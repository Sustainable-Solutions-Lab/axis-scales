"""axis_scales: tick marks and bounds for compressed (asinh / asinh2) plot axes.

Covers four kinds of axis:

- linear axes with "nice" round ticks;
- ratio axes (1.0 = no change) on a log scale, labeled in percent change;
- compressed ratio axes: asinh or asinh2 of the log ratio, labeled in
  percent, for data from near-total collapse (-99.99999%) to huge increases
  (+10^12%);
- amount axes (positive, negative or zero) on an asinh or asinh2 scale.

Everything public is re-exported here, so callers write e.g.

    from axis_scales import get_axis_bounds_and_ticks_ratio_compressed

See README.md for the math and for how to choose `scale` and `kind`.
"""

__version__ = "0.1.0"

from .asinh_transforms import (
    ASINH_KINDS,
    asinh_transform,
    asinh_inverse,
    choose_ladder_ticks,
)
from .ratio_percent_ticks import (
    percent_to_log,
    log_to_percent,
    ratio_to_percent,
    format_percent,
    format_percent_wide,
    choose_ratio_percent_ticks,
    get_axis_bounds_and_ticks_ratio_pct,
    ratio_axis_transform,
    ratio_axis_inverse,
    choose_compressed_ratio_ticks,
    get_axis_bounds_and_ticks_ratio_compressed,
)
from .amount_arcsinh_ticks import (
    amount_to_arcsinh,
    arcsinh_to_amount,
    format_amount,
    choose_amount_arcsinh_ticks,
    get_axis_bounds_and_ticks_arcsinh,
)
from .plotting import (
    RATIO_AXIS_KINDS,
    get_axis_bounds_and_ticks,
    plot_ratios,
    plot_ratios_shaded,
    plot_amounts_arcsinh,
    plot_amounts_shaded_arcsinh,
)

__all__ = [
    "ASINH_KINDS", "asinh_transform", "asinh_inverse", "choose_ladder_ticks",
    "percent_to_log", "log_to_percent", "ratio_to_percent", "format_percent",
    "format_percent_wide", "choose_ratio_percent_ticks",
    "get_axis_bounds_and_ticks_ratio_pct", "ratio_axis_transform",
    "ratio_axis_inverse", "choose_compressed_ratio_ticks",
    "get_axis_bounds_and_ticks_ratio_compressed",
    "amount_to_arcsinh", "arcsinh_to_amount", "format_amount",
    "choose_amount_arcsinh_ticks", "get_axis_bounds_and_ticks_arcsinh",
    "RATIO_AXIS_KINDS", "get_axis_bounds_and_ticks", "plot_ratios",
    "plot_ratios_shaded", "plot_amounts_arcsinh", "plot_amounts_shaded_arcsinh",
]
