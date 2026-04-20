# Effective Quaternion Geometric Field Theory (EQGFT)

**Author:** AbstractMind  
**Profile:** https://github.com/Abstract-Mindfreak/  

This repository contains the formal JSON specification of the **Effective Quaternion Geometric Field Theory (EQGFT)** in version **2.1**.

EQGFT is an effective field-theoretic reformulation of the Dirac–Maxwell sector in terms of a **physical unit-quaternion rotor field** \( Q(x) \in S^3 \subset \mathbb{H} \), interpreted as the spatial restriction of the **Dirac–Hestenes rotor** in Spacetime Algebra (STA). Mass, charge, spin, and Fermi statistics are encoded in the geometry and topology of \( Q(x) \).

> This JSON structure, naming scheme, and specific set of mechanisms and predictions (topological zitterbewegung polarization asymmetry, geometric g−2 correction, critical-field mass nonlinearity, Hopfion solitons with screening, etc.) are an original construction by **AbstractMind** and must not be confused with other quaternionic or geometric field theories.

## Repository contents

- `EQGFT_v2.1.en.json` – canonical JSON specification in English.
- `EQGFT_v2.1.ru.json` – optional Russian-localized version (if present).
- `docs/overview.en.md` – extended explanation and derivations (in progress).
- `docs/overview.ru.md` – same, in Russian (in progress).

## Concept summary

- **Fundamental field:**  
  A physical unit quaternion rotor field `Q(x)` with target space `S^3`, constrained by `Q†Q = 1`.  
  It encodes local spin orientation; gradients of `Q` measure the rate of change of the intrinsic spin frame.

- **Dirac spinor as derived object:**  
  The Dirac spinor is reconstructed as  
  \[
    \psi(x) = \mathcal{U}[Q(x)] \chi,
  \]  
  where `χ` is a constant “vacuum seed” spinor and  
  \[
    \mathcal{U}[Q] \in \mathrm{SU}(2)
  \]  
  is built from the components of `Q`. Standard Dirac theory is recovered when `Q` is constant.

- **Action:**  
  The EQGFT action contains:
  - Einstein–Hilbert gravity,
  - kinetic and constraint terms for `Q`,
  - Dirac term with **geometric mass** `m(Q) = m₀ Re(Q)`,
  - Maxwell term for `A_μ`,
  - coupling to a **geometric topological current** `J^μ_geom`.

- **Topology and quantization:**
  - Charge quantization from `π₃(S³) = ℤ` and Hopf charge `N_H`.
  - Fermi statistics from the topology of the rotor configuration space.
  - Fine structure constant `α` related to the mass scale `M` of rotor excitations.

- **Status:**  
  EQGFT is formulated as a **formal effective field theory with unique, quantitative predictions** that are, in principle, testable with near-term high-precision experiments (trapped-ion simulations, electron g−2, ultra-strong laser facilities, XFEL-based γ−γ scattering).

See `EQGFT_v2.1.en.json` for the full machine-readable specification.

## Visualization scripts

- `src/visualize_Q_field.py` – simple scripts to:
  - sample random rotor configurations Q(x) on S^3,
  - visualize their 3D projection,
  - show an example of a knotted / Hopf-like curve in R^3.
---

# Эффективная Кватернионная Геометрическая Теория Поля (EQGFT)

**Автор:** AbstractMind  
**Профиль:** https://github.com/Abstract-Mindfreak/  

В этом репозитории лежит формальная JSON‑спецификация **Effective Quaternion Geometric Field Theory (EQGFT)** версии **2.1**.

EQGFT — это эффективная полевая переформулировка сектора Дирак–Максвелл через **физическое поле единичного кватернионного ротора** \( Q(x) \in S^3 \subset \mathbb{H} \), понимаемое как пространственное ограничение **ротора Дирака–Хестенеса** в Spacetime Algebra (STA). Масса, заряд, спин и ферми‑статистика кодируются в геометрии и топологии поля \( Q(x) \).

> Данная JSON‑структура, схема имён и конкретный набор механизмов и предсказаний (асимметрия топологического zitterbewegung по поляризации, геометрический вклад в g−2, нелинейность массы в критических полях, хопфионы с экранированием и т.п.) являются оригинальной конструкцией **AbstractMind** и не должны смешиваться с другими кватернионными или геометрическими теориями поля.

## Содержимое репозитория

- `EQGFT_v2.1.en.json` – каноническая JSON‑спецификация на английском.
- `EQGFT_v2.1.ru.json` – опциональная русская версия (если присутствует).
- `docs/overview.en.md` – расширённое объяснение и выводы (в разработке).
- `docs/overview.ru.md` – то же на русском (в разработке).

## Краткое описание концепции

- **Фундаментальное поле:**  
  Физическое поле единичного кватернионного ротора `Q(x)` со значениями в `S^3`, с ограничением `Q†Q = 1`.  
  Оно кодирует локальную ориентацию спина; градиенты `Q` измеряют скорость изменения внутренней спиновой рамки.

- **Спинор Дирака как производная величина:**  
  Спинор Дирака восстанавливается как  
  \[
    \psi(x) = \mathcal{U}[Q(x)] \chi,
  \]  
  где `χ` — постоянный «вакуумный» спинор, а  
  \[
    \mathcal{U}[Q] \in \mathrm{SU}(2)
  \]  
  строится из компонент `Q`. При постоянном `Q` стандартная теория Дирака полностью воспроизводится.

- **Действие:**  
  Действие EQGFT включает:
  - гравитационный член Эйнштейна–Гильберта,
  - кинетический и ограничивающий члены для `Q`,
  - дираковский член с **геометрической массой** `m(Q) = m₀ Re(Q)`,
  - максвелловский член для `A_μ`,
  - связь с **топологическим геометрическим током** `J^μ_geom`.

- **Топология и квантизация:**
  - Квантизация заряда из `π₃(S³) = ℤ` и числа Хопфа `N_H`.
  - Ферми‑статистика как следствие топологии конфигурационного пространства роторов.
  - Постоянная тонкой структуры `α` связана с масштабом массы `M` возбуждений ротора.

- **Статус:**  
  EQGFT сформулирована как **формальная эффективная теория поля с уникальными количественными предсказаниями**, которые, в принципе, могут быть проверены в ближайших высокоточных экспериментах (квантовые симуляторы на ионах, g−2 электрона, ультрамощные лазерные установки, γ−γ‑рассеяние на XFEL).

Подробности см. в `EQGFT_v2.1.en.json`.
