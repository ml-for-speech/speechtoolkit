from setuptools import setup, find_packages

extras = {
    'vc': [
        'lvc',
        'ns3vc',
    ],
    'asr': [
        'openai-whisper',
    ],

    'dev': [
        'mkdocs',
        'mkautodoc',
    ]
}

extra_pkgs = extras
final = []

for k, v in extras:
    if not k == 'dev':
        final.append(v)

extra_pkgs['all'] = list(set(final))

with open("README.md", "r") as f:
    longdesc = f.read()
setup(
    name="speechtoolkit",
    version="0.0.0",
    author="ml-for-speech",
    description="ML for Speech presents SpeechToolkit, a unified, all-in-one toolkit for TTS, ASR, VC, & other models.",
    long_description=longdesc,
    long_description_content_type="text/markdown",
    url="https://github.com/ml-for-speech/speechtoolkit",
    packages=find_packages(),
    install_requires=[
        'soundfile',
        'librosa',
        'torch',
        'transformers',
    ],
    extras_require=extra_pkgs,
)