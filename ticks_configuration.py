from matplotlib.ticker import AutoMinorLocator


def setup_minor_ticks(
    ax,
    x_minor_divisions=4, y_minor_divisions=2,
    major=(14, 2.5), minor=(8, 1.2),
    sides=dict(top=True, right=True, bottom=True, left=True),
    direction_top='in',
    direction_bottom='out',
    direction_left='in',
    direction_right='in'
):
    # Enable and configure minor tick locators for both axes
    ax.minorticks_on()
    ax.xaxis.set_minor_locator(AutoMinorLocator(x_minor_divisions))
    ax.yaxis.set_minor_locator(AutoMinorLocator(y_minor_divisions))

    # Unpack major and minor tick styling parameters
    major_length, major_width = major
    minor_length, minor_width = minor

    # Apply tick styling for all sides and levels (major and minor)
    # to allow fine-grained, reusable control over axis appearance
    ax.tick_params(axis='x', which='major', length=major_length, width=major_width,
                   direction=direction_top, top=sides['top'])
    ax.tick_params(axis='x', which='major', length=major_length, width=major_width,
                   direction=direction_bottom, bottom=sides['bottom'])

    ax.tick_params(axis='y', which='major', length=major_length, width=major_width,
                   direction=direction_left, left=sides['left'])
    ax.tick_params(axis='y', which='major', length=major_length, width=major_width,
                   direction=direction_right, right=sides['right'])

    ax.tick_params(axis='x', which='minor', length=minor_length, width=minor_width,
                   direction=direction_top, top=sides['top'])
    ax.tick_params(axis='x', which='minor', length=minor_length, width=minor_width,
                   direction=direction_bottom, bottom=sides['bottom'])

    ax.tick_params(axis='y', which='minor', length=minor_length, width=minor_width,
                   direction=direction_left, left=sides['left'])
    ax.tick_params(axis='y', which='minor', length=minor_length, width=minor_width,
                   direction=direction_right, right=sides['right'])