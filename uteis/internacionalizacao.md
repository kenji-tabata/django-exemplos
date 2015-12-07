Internacionalização do Django
===

Settings.py
---

Adicione o middleware

    'django.middleware.locale.LocaleMiddleware',

Adicione os idiomas utilizados na internacionalização

    # Evite utilizar ugettext no settings para não criar o po dele
    ugettext = lambda s: s

    LANGUAGES = (
        ('pt_BR', ugettext('Portugues brasileiro')),
        ('en_US', ugettext('English')),
        ('es', ugettext('Spanish')),
    )

    LANGUAGES = (
        ('pt_BR', ('Portugues brasileiro')),
        ('en_US', ('English')),
        ('es', ('Spanish')),
    )

Define quais pastas terão que utilizar o recurso

    LOCALE_PATHS = [
        os.path.join(BASE_DIR, "formularios/locale"),
    ]

No template utilize

{% load i18n %} = no topo para utilizar a internacionalização

Nos textos de uma linha = {% trans 'Insira o texto aqui' %}

Crie as pastas...

    locale
        pt_BR
            LC_MESSAGES

Execute o comando para gerar os arquivos po

    python manage.py makemessages -l es -l en

Execute o comando para gerar os arquivos de tradução mo

    python manage.py compilemessages -l es -l en

Em urls.py da aplicação principal adicione

    url(r'^i18n/', include('django.conf.urls.i18n', namespace="idioma")),

Formulário para trocar de idioma

{% get_available_languages as LANGUAGES %}
{% get_current_language as LANGUAGE_CODE %}
<form action="{% url 'idioma:set_language' %}" method="post">
    {% csrf_token %}
    <input name="next" type="hidden" value="" />
    <select name="language" id="language">
        <option value="" selected="true">{% trans 'Selecione o idioma' %}</option>
        <option class="divider"></option>
        {% get_language_info_list for LANGUAGES as languages %}
        {% for language in languages %}
            <option value="{{ language.code }}"{% if language.code == LANGUAGE_CODE %} selected="selected"{% endif %}>
                {{ language.name_local }}
            </option>
        {% endfor %}
    </select>
    <input type="submit" value="Go" />                    
    </p>
</form>