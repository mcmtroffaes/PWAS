
import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pwas',
    version='0.0.1',
    author= 'Mengjia Zhu, Alberto Bemporad',
    author_email='mengjia.zhu@imtlucca.it, alberto.bemporad@imtlucca.it',
    description='PWAS/PWASp - Global and Preference-based Optimization with Mixed Variables using (P)iece(w)ise (A)ffine (S)urrogates',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mjzhu-p/PWAS',
    project_urls = {
        "PWAS/PWASp": "https://github.com/mjzhu-p/PWAS"
    },
    license='Apache-2.0',
    py_modules=['src/pwas'],
    install_requires=['numpy','scipy','math','pulp','sklearn','pyDOE','cdd'],
)