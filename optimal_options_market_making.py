import holoviews as hv
import numpy as np
from scipy.integrate import solve_ivp
from fyne import heston


_EPS = 1.e-12


def optimal_controls(time, inventory_bounds, price_risk_aversion,
                     exec_risk_aversion, base_intensities, intensity_decays,
                     covariance_matrix):
    t = time
    Q = inventory_bounds
    γ = price_risk_aversion
    ξ = exec_risk_aversion
    A = base_intensities
    k = intensity_decays
    Σ = covariance_matrix

    d = len(A)
    C = (1 + ξ/k)**-(1 + k/ξ) if ξ > _EPS else np.exp(-np.ones(d))
    η = A*C

    q = np.stack(np.meshgrid(*(np.arange(-Qi, Qi + 1) for Qi in Q),
                             indexing='ij'), axis=-1)
    ẏ0 = -γ*(q.dot(Σ)*q).sum(axis=-1)/2

    Ib = np.full((d, d), slice(None))
    Ia = Ib.copy()
    np.fill_diagonal(Ia, slice(1, None))
    np.fill_diagonal(Ib, slice(None, -1))
    Ia = list(map(tuple, Ia))
    Ib = list(map(tuple, Ib))

    sol = solve_ivp(multiasset_ode_rhs(ẏ0, Ib, Ia, η, k, Q), (0, t),
                    np.zeros(ẏ0.shape).ravel())
    θ = np.reshape(sol.y[:, -1], ẏ0.shape)

    δ_b = np.full(q.shape, np.nan)
    δ_a = np.full(q.shape, np.nan)
    for i in range(d):
        Hb = η[i]*np.exp(-k[i]*(θ[Ib[i]] - θ[Ia[i]]))/k[i]
        Ha = η[i]*np.exp(-k[i]*(θ[Ia[i]] - θ[Ib[i]]))/k[i]

        δ_b[(*Ib[i], i)] = -np.log((ξ*Hb + k[i]*Hb)/A[i])/k[i]
        δ_a[(*Ia[i], i)] = -np.log((ξ*Ha + k[i]*Ha)/A[i])/k[i]

    return δ_b, δ_a


def multiasset_ode_rhs(ẏ0, Ib, Ia, η, k, Q):
    def closure(t, y):
        y = np.reshape(y, ẏ0.shape)

        ẏ = ẏ0.copy()
        for i in range(len(Q)):
            Hb = η[i]*np.exp(-k[i]*(y[Ib[i]] - y[Ia[i]]))/k[i]
            Ha = η[i]*np.exp(-k[i]*(y[Ia[i]] - y[Ib[i]]))/k[i]
            ẏ[Ib[i]] += Hb
            ẏ[Ia[i]] += Ha

        return ẏ.ravel()

    return closure


def options_cov_matrix(underlying_price, strikes, expiry, vol, kappa, theta,
                       nu, rho):
    deltas = heston.delta(underlying_price, strikes, expiry, vol, kappa, theta,
                          nu, rho)
    vegas = heston.vega(underlying_price, strikes, expiry, vol, kappa, theta,
                        nu, rho)

    greeks = np.stack([deltas, vegas], axis=-1)
    rho_mat = np.array([[1, rho], [rho, 1]])
    vol_vec = np.array([np.sqrt(vol)*underlying_price, nu])

    factors_cov_mat = rho_mat * vol_vec[:, None].dot(vol_vec[None, :])
    return greeks @ factors_cov_mat @ greeks.T


kappa = 5.07
theta = 0.0457
nu = 0.48
rho = -0.767
mu = 3.9*np.sqrt(1 - rho**2)

underlying_price = 1640
vol = theta

strikes = np.array([0.8, 1, 1.2])*underlying_price
expiry = 1/12
cov_matrix = options_cov_matrix(underlying_price, strikes, expiry, vol, kappa,
                                theta, nu, rho)/(365*6*60)

params = dict(time=10, inventory_bounds=(20, 20, 20),
              covariance_matrix=cov_matrix, base_intensities=np.array(3*[0.9]),
              intensity_decays=np.array(3*[0.3]), exec_risk_aversion=0.01,
              price_risk_aversion=0.01)

inventory = np.arange(-20, 21)
bid_control, ask_control = optimal_controls(**params)

data = (['ITM', 'ATM', 'OTM'], inventory, inventory, inventory, ['Bid', 'Ask'],
        (underlying_price - bid_control, underlying_price + ask_control))
kdims = ['Option', hv.Dimension('OTM inventory', default=0), 'ATM inventory',
         hv.Dimension('ITM inventory', default=0), 'Quote']
ds = hv.Dataset(data, kdims, 'Price')

hv.extension('bokeh')
hv.output(max_frames=6000)
curve = ds.to(hv.Curve, 'ATM inventory', 'Price'
         ).overlay('Quote'
         ).opts(responsive=True, height=720, title='Optimal quotes')
hv.save(curve, '20190716/optimal_quotes.html')
