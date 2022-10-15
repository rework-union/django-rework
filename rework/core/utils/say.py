def say(content, icon=None, wrap=''):
    """convenient way to output message

    `wrap` choices is
        'A' - append wrap after content,
        'B' - before content,
        'C' - both
    """
    leading = f'{icon:3}' if icon else ' ▪  '
    wrap = wrap.upper()
    if wrap in ['B', 'C']:
        print()

    print('{}{}'.format(leading, content))

    if wrap in ['A', 'C']:
        print()


def patch_connection_with_say(connection):

    origin_connection_run = connection.run

    def patched_run(command, **kwargs):
        say(command, icon='🥤')
        return origin_connection_run(command, **kwargs)

    connection.run = patched_run

    return connection
