{# Cover page of the PDF / print version. Jinja template, rendered by
   mkdocs-print-site-plugin; `config` is the mkdocs.yml config. #}
<div class="rotse-cover">
  <img class="rotse-cover-logo" src="../assets/rotse.png" alt="ROTSE logo">
  <h1>{{ config.site_name }}</h1>
  <p class="rotse-cover-sub">{{ config.site_description }}</p>

  <table class="rotse-cover-meta">
    <tr><td>Version</td><td>{{ config.extra.manual_version }}</td></tr>
    <tr><td>Date</td><td>{{ config.extra.manual_date }}</td></tr>
    {% if config.site_author %}<tr><td>Maintained by</td><td>{{ config.site_author }}</td></tr>{% endif %}
    {% if config.site_url %}<tr><td>Current version</td><td><a href="{{ config.site_url }}">{{ config.site_url }}</a></td></tr>{% endif %}
  </table>

  <p class="rotse-cover-note">
    This is a printed copy and may be out of date.
    {% if config.site_url %}Always check the online version before observing.{% endif %}
  </p>
</div>
