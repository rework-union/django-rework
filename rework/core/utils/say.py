def say(content, icon=None, wrap=''):
    """convenient way to output message

    `wrap` choices is
        'A' - append wrap after content,
        'B' - before content,
        'C' - both
    """
    leading = f'{icon} ' if icon else '  - '
    wrap = wrap.upper()
    if wrap in ['B', 'C']:
        print()

    print('{}{}'.format(leading, content))

    if wrap in ['A', 'C']:
        print()
