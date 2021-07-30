import re

from rework.core.utils import get_root_urls_path


class UrlsHandle:
    """
    Handle django app's urls
    """
    def __init__(self, app=None):
        self.app = app  # When app is None, target to root urls

    @staticmethod
    def _save(f, content):
        f.seek(0)
        f.truncate()
        f.write(content)

    def add_include_urls(self, namespace):
        """
        Add include urls like:

            re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

        """
        if self.app:
            raise NotImplemented

        # Get the root urls file
        urls_file = get_root_urls_path()
        with open(urls_file, 'r+') as f:
            content = f.read()
            content = self._add_route(content, namespace)
            self._save(f, content)

    def _add_route(self, content, namespace):
        rule = f"    re_path(r'^api/{namespace}/', include('rework.contrib.{namespace}.urls')),\n"
        pattern = r'urlpatterns = \[\n([^\n]*\n)*\]\n'
        match = re.search(pattern, content)
        if not match:
            print('There is no `urlpatterns` block in your urls')
            return False

        # get exists rules
        rules = list(match.groups())
        rules.append(rule)

        urlpatterns_block = f'urlpatterns = [\n{"".join(rules)}]\n'

        # make sure import re_path
        if 're_path' not in content:
            urlpatterns_block = f'from django.urls import re_path, include\n\n{urlpatterns_block}'

        content = re.sub(pattern, urlpatterns_block, content)

        return content
