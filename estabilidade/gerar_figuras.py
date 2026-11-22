#!/usr/bin/env python3
"""
Gera as figuras da parte de Estabilidade (Projeto 2 - EDO).
Estilo visual casado com o deck da Camilla (Canva):
  fundo creme #fffeec, azul #2a78d6 (linearizado), laranja #e8622a (nao-linear).
Parametros do problema: L = k = m = 1 (como no item 2c da Camilla).

Sistema:  m x'' + f(x) = 0,  f(x) = 2k x (1 - L / sqrt((L+h)^2 + x^2)).
Em primeira ordem:  y1 = x, y2 = x'  ->  y1' = y2,  y2' = -f(y1)/m.
"""
import os
os.environ.setdefault("MPLCONFIGDIR", "/tmp/mplconfig")
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams

# ----- paleta do deck -----
CREME   = "#fffeec"
SLATE   = "#5b6975"
AZUL    = "#2a78d6"   # linearizado
LARANJA = "#e8622a"   # nao-linear
TINTA   = "#2b2b2b"

rcParams.update({
    "figure.facecolor": CREME,
    "axes.facecolor": CREME,
    "savefig.facecolor": CREME,
    "font.family": "DejaVu Sans",
    "mathtext.fontset": "cm",
    "axes.edgecolor": SLATE,
    "axes.labelcolor": TINTA,
    "xtick.color": TINTA,
    "ytick.color": TINTA,
    "text.color": TINTA,
    "axes.linewidth": 1.1,
    "font.size": 15,
})

OUT = os.path.join(os.path.dirname(__file__), "figuras")
os.makedirs(OUT, exist_ok=True)

L = k = m = 1.0

def f(x, h):
    a = L + h
    return 2*k*x*(1 - L/np.sqrt(a**2 + x**2))

def V(x, h):
    """Potencial V(x) = integral de f de 0 a x = k x^2 - 2kL(sqrt(a^2+x^2)-a)."""
    a = L + h
    return k*x**2 - 2*k*L*(np.sqrt(a**2 + x**2) - a)

def deriv(Y, h):
    y1, y2 = Y
    return np.array([y2, -f(y1, h)/m])

def orbit(x0, v0, h, tmax=40, n=6000):
    """Integra o sistema por RK4 para traçar uma orbita no plano de fases."""
    t = np.linspace(0, tmax, n)
    dt = t[1]-t[0]
    Y = np.zeros((n, 2))
    Y[0] = [x0, v0]
    for i in range(n-1):
        y = Y[i]
        k1 = deriv(y, h)
        k2 = deriv(y + dt/2*k1, h)
        k3 = deriv(y + dt/2*k2, h)
        k4 = deriv(y + dt*k3, h)
        Y[i+1] = y + dt/6*(k1 + 2*k2 + 2*k3 + k4)
    return Y[:,0], Y[:,1]

def style_axes(ax):
    ax.grid(True, color=SLATE, alpha=0.18, linewidth=0.8)
    for s in ax.spines.values():
        s.set_color(SLATE)

# =====================================================================
# FIG 1 - Plano de fases do sistema LINEARIZADO (h>0): elipses -> centro
# =====================================================================
def fig1():
    h = 0.5
    w2 = 2*k*h/(m*(L+h))          # omega^2
    w = np.sqrt(w2)
    fig, ax = plt.subplots(figsize=(6.2, 5.6))
    th = np.linspace(0, 2*np.pi, 400)
    for A in [0.3, 0.55, 0.8, 1.05]:
        # orbita do linearizado: w^2 x^2 + v^2 = const -> elipse
        x = A*np.cos(th)
        v = -A*w*np.sin(th)
        ax.plot(x, v, color=AZUL, lw=3.0)
        # seta de sentido (horario) no topo
        xi = int(len(th)*0.0)
        ax.annotate("", xy=(x[5], v[5]), xytext=(x[0], v[0]),
                    arrowprops=dict(arrowstyle="-|>", color=AZUL, lw=3.0, mutation_scale=22))
    ax.plot(0, 0, "o", color=SLATE, ms=10)
    ax.annotate("equilíbrio\n(centro)", xy=(0,0), xytext=(0.45,-0.28),
                fontsize=14, color=TINTA,
                arrowprops=dict(arrowstyle="-", color=SLATE, lw=1.0))
    ax.set_xlabel(r"$x$", fontsize=18)
    ax.set_ylabel(r"$v = x'$", fontsize=18)
    ax.set_title(r"Sistema linearizado ($h=0{,}5$): elipses concêntricas",
                 fontsize=16, color=TINTA, pad=12)
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.2, 1.2)
    ax.set_aspect(1.5/1.2)
    style_axes(ax)
    fig.tight_layout()
    fig.savefig(f"{OUT}/fig1_fase_linear.png", dpi=200)
    plt.close(fig)
    print("fig1 ok  (omega =", round(w,4), ")")

# =====================================================================
# FIG 2 - Plano de fases: linearizado (elipses) x nao-linear (orbitas)
# =====================================================================
def fig2():
    h = 0.5
    w2 = 2*k*h/(m*(L+h)); w = np.sqrt(w2)
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 5.2))
    th = np.linspace(0, 2*np.pi, 400)
    for A in [0.3, 0.6, 0.9, 1.2]:
        x = A*np.cos(th); v = -A*w*np.sin(th)
        axL.plot(x, v, color=AZUL, lw=2.6)
    for x0 in [0.3, 0.6, 0.9, 1.2]:
        x, v = orbit(x0, 0.0, h, tmax=30, n=5000)
        axR.plot(x, v, color=LARANJA, lw=2.6)
    for ax, ttl in [(axL, r"Linearizado: $\omega^2 x^2 + v^2 = $ const"),
                    (axR, r"Não-linear: $m x'' + f(x) = 0$")]:
        ax.plot(0,0,"o",color=SLATE, ms=8)
        ax.set_xlabel(r"$x$", fontsize=17)
        ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.2, 1.2)
        ax.set_title(ttl, fontsize=15, color=TINTA, pad=10)
        style_axes(ax)
    axL.set_ylabel(r"$v = x'$", fontsize=17)
    fig.suptitle(r"Órbitas fechadas em torno de $(0,0)$ — $h=0{,}5$",
                 fontsize=16, color=TINTA, y=1.0)
    fig.tight_layout()
    fig.savefig(f"{OUT}/fig2_fase_comparacao.png", dpi=200)
    plt.close(fig)
    print("fig2 ok")

# =====================================================================
# FIG 3 - Potencial V(x): nao-linear x aproximacao quadratica, varios h
# =====================================================================
def fig3():
    x = np.linspace(-1.5, 1.5, 600)
    hs = [1.0, 0.5, 0.1, 0.0]
    labels = [r"$h=1{,}0$", r"$h=0{,}5$", r"$h=0{,}1$", r"$h=0$"]
    fig, axes = plt.subplots(2, 2, figsize=(10, 7), sharex=True)
    for ax, h, lab in zip(axes.ravel(), hs, labels):
        Vnl = V(x, h)
        a = L + h
        fp0 = 2*k*h/a                 # f'(0) = 2kh/(L+h)
        Vlin = 0.5*fp0*x**2
        ax.plot(x, Vnl, color=LARANJA, lw=3.0, label=r"$V(x)$ (não-linear)")
        ax.plot(x, Vlin, color=AZUL, lw=3.0, ls="--",
                label=r"$V_{\mathrm{lin}}(x)=\frac{f'(0)}{2}x^2$")
        ax.text(0.04, 0.88, lab, transform=ax.transAxes, fontsize=16, color=TINTA)
        ax.set_ylim(-0.05, 1.5)
        style_axes(ax)
    axes[1,0].set_xlabel(r"$x$", fontsize=16)
    axes[1,1].set_xlabel(r"$x$", fontsize=16)
    axes[0,0].set_ylabel("energia potencial", fontsize=14)
    axes[1,0].set_ylabel("energia potencial", fontsize=14)
    axes[0,0].legend(loc="upper center", fontsize=12, framealpha=0.9)
    fig.tight_layout()
    fig.savefig(f"{OUT}/fig3_potencial.png", dpi=200)
    plt.close(fig)
    print("fig3 ok")

# =====================================================================
# FIG 4 - Caso h=0: linearizado (x''=0, retas) x nao-linear (orbitas fechadas)
# =====================================================================
def fig4():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 5.0))
    # LINEARIZADO h=0: x''=0 => v=const. Fluxo horizontal; v=0 todos equilibrios.
    xs = np.linspace(-1.6, 1.6, 2)
    for v0 in [0.8, 0.5, 0.25, -0.25, -0.5, -0.8]:
        axL.plot(xs, [v0, v0], color=AZUL, lw=2.6)
        d = 0.001 if v0 > 0 else -0.001
        axL.annotate("", xy=(0.0+np.sign(v0)*0.05, v0), xytext=(0.0, v0),
                     arrowprops=dict(arrowstyle="-|>", color=AZUL, lw=2.6, mutation_scale=20))
    axL.plot([-1.6,1.6],[0,0], color=AZUL, lw=5.0)
    axL.text(-1.5, 0.12, r"todos os pontos de $v=0$ são equilíbrios",
             fontsize=12.5, color=TINTA)
    # NAO-LINEAR h=0: m x'' + (k/L^2) x^3 = 0 (orbitas fechadas)
    for x0 in [0.4, 0.7, 1.0, 1.3]:
        x, v = orbit(x0, 0.0, 0.0, tmax=30, n=6000)
        axR.plot(x, v, color=LARANJA, lw=2.6)
    axR.plot(0,0,"o",color=SLATE, ms=8)
    for ax in (axL, axR):
        ax.set_xlabel(r"$x$", fontsize=17)
        ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.0, 1.0)
        style_axes(ax)
    axL.set_ylabel(r"$v = x'$", fontsize=17)
    axL.set_title(r"Linearizado ($h=0$): $x''=0$", fontsize=15, color=TINTA, pad=10)
    axR.set_title(r"Não-linear ($h=0$): $m x'' + \frac{k}{L^2}x^3 = 0$",
                  fontsize=15, color=TINTA, pad=10)
    fig.tight_layout()
    fig.savefig(f"{OUT}/fig4_caso_h0.png", dpi=200)
    plt.close(fig)
    print("fig4 ok")

if __name__ == "__main__":
    fig1(); fig2(); fig3(); fig4()
    print("Figuras geradas em", OUT)
