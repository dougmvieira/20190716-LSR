---
title: <small> High-frequency options market making </small>
author:
- <b> Late stage review </b>
- Douglas Vieira
- Imperial College London
- Supervisors&colon; Prof Rama Cont and Dr Mikko Pakkanen
date: 16 July 2019
---


# Introduction

## Outline

- Options market making model I
  - Incorporate option price dynamics in a market making framework

- Options market microstructure
  - Linearity of option prices in small time scales
  - Role of stochastic volatility
  - Structure of trade activity

- Options market making model II
  - Future research
  - Aiming at closed-form solutions without heuristic approximations
  - Incorporate trade activity structure in a market making framework

## Motivation

- Gap in the literature
  - Known studies: [@stoikov2009option] and [@el2015stochastic]
  
- Focus on high-frequency market making

- Combine option pricing theory with optimal market making

- Understand the role of stochastic volatility


# Options market making model I
  
## Approach

#. Start with price dynamics from option theory
#. Find local behaviour via small time asymptotics
#. Incorporate local dynamics to market making model

## Small time asymptotics

*Theorem* Let $X$ be an Itô diffusion, of the form

$$ dX_t = \mu_t dt + \sigma_t dW_t, $$

$$ \text{then } \frac{X_t - \tilde X_t}{\sqrt t} \xrightarrow{L^2} 0, \text{ as } t\to 0,$$

$$ \text{where } d\tilde X_t = \sigma_0 dW_t. $$

## {data-background-iframe="20180528/heston.html"}

## Option representation

*Theorem.* Assume the market state process $X$ is an Itô diffusion with locally
Lipschitz coefficients, invertible diffusion coefficient matrix and with open
connected support. Then, under no arbitrage, the option $C$ with
square-integrable payoff $f(X_T)$ follows

$$ C_t = \varphi(X_t), \quad dC_t = \nabla_x\varphi(X_t)dX_t, $$

$$ \text{where } \varphi(x) = \mathbb E^{\mathbb Q}[f(X_T)\mid X_t=x]. $$

## Role of stochastic volatility

- Applying small time asymptotics to option prices,

$$ d\tilde C_t = \nabla_x\varphi(X_0) d\tilde X_t $$

- In particular, if the market state is $(S, V)$,

$$ d\tilde C_t = \Delta_0 d\tilde S_t + \mathcal{V}_0 d\tilde V_t$$

- Options still depend on volatility
  - Despite prices losing stochastic volatility
  - Volatility links different time scales

## Market making framework

- Following [@gueant2017optimal]

- Bid and ask quotes $S^\mathrm{ask}_t$ and $S^\mathrm{bid}_t$ are posted around
  a reference price

$$ dS_t^i = \sigma^i dW_t^i, \quad d[W^i, W^j]_t = \rho^{ij}dt $$

- Trades at bid and ask prices are point processes with arrival rates

$$ \Lambda^{i, \mathrm{ask}}_t = \Lambda^i(S^{i, \mathrm{ask}}_t - S_t^i), \quad
   \Lambda^{i, \mathrm{bid}}_t = \Lambda^i(S^{i, \mathrm{bid}}_t - S_t^i) $$
$$ \Lambda^i(\delta) = A^ie^{-k^i\delta} $$

## {data-background-iframe="20190226/skew_plot.html"}

## {data-background-iframe="20190226/spread_plot.html"}

## Optimisation problem

- Market maker optimises CARA utility on terminal wealth with risk aversion
  parameter $\gamma$ and liquidity penalty $\ell$

- The HJB equation is transformed to the system of ODEs
<small>
$$ \begin{align}
\partial_t \theta(t, q) = & \frac{1}{2} \gamma \sum_{i=1}^d\sum_{j=1}^d \rho^{i,j} \sigma^i\sigma^j q^i q^j
  - \sum_{i=1}^d 1_{q^i<Q^i}\frac{A^i C_\gamma^i}{k} \exp\left(-k^i\left(\theta\left(t, q\right) - \theta\left(t, q + e^i\right)\right)\right) \\
& - \sum_{i=1}^d  1_{q^i>-Q^i}\frac{A^i C_\gamma^i}{k} \exp\left(-k^i\left(\theta\left(t, q\right) - \theta\left(t, q - e^i\right)\right)\right), \\
\theta(T, q) = & -\ell(q).
\end{align} $$
</small>

## Approximate solution

- Approximation for $T \to \infty$ and by 2nd order Taylor expansion on the
  difference term

- Optimal spread is constant
$$ S^{i,\mathrm{ask}}_t - S^{i,\mathrm{bid}}_t = \frac{2}{\gamma}
  \log\left(1+\frac{\gamma}{k^{i}}\right)
  + \sqrt{\frac{\gamma}{2}}\Gamma^{ii} $$

- Optimal skew is linear
$$ \frac{S^{i,\mathrm{ask}}_t + S^{i,\mathrm{bid}}_t}{2} - S^i_t
= -\sqrt{\frac{\gamma}{2}}\Gamma^{i\bullet} q_{t-}, $$

## 

where
$$ \Gamma = D^{-\frac 1 2}(D^{1/2}\Sigma D^{1/2})^{1/2} D^{-\frac 1 2} $$
$$ D = \text{diag}(A^1 C_\gamma^1 k^1,
           \ldots, A^d C_\gamma^d k^d), $$
$$ C_\gamma^i = \left(1+\frac{\gamma}{k^{i}}
    \right)^{-\left(1+\frac{k^{i}}{\gamma}\right)} $$

## {data-background-iframe="20190716/optimal_quotes.html"}


# Options market microstructure

## Market microstructure effects

- Fundamental price vs microstructure price
  - Market maker needs to filter microstructure effects

- Options are unevenly affected by microstructure effects

## Intraday volatility

- Stochastic volatility is obtained by inverting the Heston formula
- Consistent with at-the-money volatility
- Stochastic volatility is rough

## {data-background-image="20190716/vols.png" data-background-size=contain}
## {data-background-image="20190716/variogram.png" data-background-size=contain}

## Linear model for options

- Approach
  #. Option representation gives option dynamics
  #. Small time asymptotics linearises option dynamics

- The linear model is
$$ C_{t+h} - C_t = \Delta(S_{t+h} - S_t) + \mathcal{V}(V_{t+h} - V_t) + \epsilon_{t+h}. $$

## Recovering Greeks

- Microstructure effects don't bias Greeks estimation

- Role of stochastic volatility
  - Contributes to explaining option price changes
  - Enhance the explanatory power of the underlying price

- Vega is successfully recovered for the first time
  - Compare with [@abergel2012drives]

## {data-background-image="20190716/compare_deltas_call.png" data-background-size=contain}
## {data-background-image="20190716/compare_vegas_call.png" data-background-size=contain}

## Trading activity structure

- Main drivers are moneyness and expiry
- Minor drivers are strike/expiry grid density and age of the option issue
- Moneyness is stochastic

## {data-background-image="20190716/trade_activity.png" data-background-size=contain}


# Options market making model II

## Ideas for tractability

- Heavy-traffic approximation on wealth process
  - Allows Hawkes-like processes for order flow
  - Optimal quotes reinterpreted as average targets
  - High dimensionality implies better approximation

- Time-homogeneous solutions
  - Market maker horizon at infinity
  - E.g. ergodic control for [@cjp15]-type of functional
$$ \lim_{T\to\infty} \frac{1}{T}\mathbb E \left[ \int_0^T\left(dV_t - \gamma d[V]_t\right) \right] $$
 
## Other ideas

- Couple trading activity between options
  - Trading activity depends on option position on the vol surface
  - Allow order flow to depend on underlying asset price
 
- Factor-based market making
  - Both price and trade activity dynamics explained by factors
  - Optimal quotes as a function of strike and expiry

## Extension

- Incorporating views
  - Views as in [@black1992global] and [@davis2013black]
  - Allows for views on linear combination of options

## Thank you!

- Find this presentation and its source code at

<https://github.com/dougmvieira/presentations>

## References {.scrollable}
