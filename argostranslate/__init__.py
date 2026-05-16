"""Argos Translate - Open-source offline translation library.

A Python library for translating text between languages using
pre-trained machine learning models. Supports offline translation
without requiring an internet connection after model installation.

Example usage::

    import argostranslate.package
    import argostranslate.translate

    # Install a language package
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = available_packages[0]
    argostranslate.package.install_from_path(package_to_install.download())

    # Translate text
    translated_text = argostranslate.translate.translate(
        "Hello, world!", "en", "es"
    )
    print(translated_text)  # "¡Hola, mundo!"

Notes (personal fork):
    - Forked for personal learning/experimentation.
    - See https://github.com/argosopentech/argos-translate for upstream.
"""

__version__ = "2.0.0"
__author__ = "Argos Open Tech"
__license__ = "MIT"
__url__ = "https://github.com/argosopentech/argos-translate"

# Package metadata
package_name = "argostranslate"
description = "Open-source offline translation library"
