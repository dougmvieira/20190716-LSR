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

## Option representation

*Lemma* Let the market state process $(X_t)_{t\in[0,T]}$ be a continuous
semimartingale. Assume the existence of an ELMM $\mathbb Q$ where
$(X_t)_{t\in[0,T]}$ is a Markov process. Then, a no-arbitrage price process
$(C_t)_{t\in[0,T]}$ of an $\mathcal F_T$-measurable claim $f(X_T) \geq 0$ is
given by
$$  C_t = \varphi(t, X_t), \quad
    \varphi(t, x) = \mathbb E^{\mathbb Q}[f(X_{T - t}) \mid X_0 = x]. $$

If $\varphi$ is of class $\mathcal C^{1, 2}(U)$, then
$$  dC_t = \nabla_x\varphi(t, X_t)dX_t, \quad \forall t \in [0, T). $$


## Small time asymptotics

*Theorem* Let $X$ be an Itô diffusion, of the form

$$ dX_t = \mu_t dt + \sigma_t dW_t, $$

$$ \text{then } \frac{X_t - \tilde X_t}{\sqrt t} \xrightarrow{L^2} 0, \text{ as } t\to 0,$$

$$ \text{where } d\tilde X_t = \sigma_0 dW_t. $$

## Heston model simulation

## {data-background-iframe="20180528/heston.html"}

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

## Options market making model I simulation

## {data-background-iframe="20190716/optimal_quotes.html"}


# Options market microstructure

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

## Heston vs Empirical Delta for call options

## {data-background-image="20190716/compare_deltas_call.png" data-background-size=contain}

## Heston vs Empirical Vega for call options

## {data-background-image="20190716/compare_vegas_call.png" data-background-size=contain}

## Trading activity structure

- Main drivers are moneyness and expiry
- Minor drivers are strike/expiry grid density and age of the option issue
- Moneyness is stochastic

## {data-background-image="20190716/trade_activity.png" data-background-size=contain}


# Options market making model II

## Ideas

- Tractability
  - Heavy-traffic approximation on wealth process
  - Time-homogeneous solutions
- Liquidity structure
  - Trading activity as function of moneyness and expiry
  - Factor-based market making (continuum of options)
- Extension
  - Views as in [@black1992global]

## Thank you!

- Find this presentation and its source code at

<https://github.com/dougmvieira/presentations>

## References {.scrollable}
