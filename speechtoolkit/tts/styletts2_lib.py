from speechtoolkit.utils.device import device_map
from txtsplit import txtsplit


class MultiSpeakerStyleTTS2Model:
    """
    Text to Speech with StyleTTS 2

    **Args**

    device (str): The device to use. Defaults to 'auto'
    **kwargs: Additional arguments to pass to Whisper package
    """

    def __init__(
        self,
        device='auto',
        **kwargs,
    ):
        """
        Initialize model.

        **Args**

        **kwargs: Additional arguments to pass to Whisper package
        """
        from mfs_styletts2.zeroshot import LFinference, compute_style
        from openphonemizer import OpenPhonemizer
        import numpy as np
        from scipy.io.wavfile import write

        self.np = np
        self.write = write
        self.LFinference = LFinference
        self.compute_style = compute_style
        self.phonemizer = OpenPhonemizer()

    def infer_to_file(
        self,
        text,
        sample,
        output,
    ):
        s_ref = self.compute_style(sample)
        sentences = txtsplit(self.phonemizer(text))
        wavs = []
        s_prev = None
        for text in sentences:
            if text.strip() == "":
                continue
            wav, s_prev = self.LFinference(
                text,
                s_prev,
                s_ref,
                alpha=0.3,
                beta=0.9,
                t=0.7,
                diffusion_steps=10,
                embedding_scale=1.1,
                phonemize=False
            )
            wavs.append(wav)
        self.write(output, 24000, self.np.concatenate(wavs))

class SingleSpeakerStyleTTS2Model:
    """
    Text to Speech with StyleTTS 2

    **Args**

    **kwargs: Additional arguments to pass to Whisper package
    """

    def __init__(
        self,
        **kwargs,
    ):
        """
        Initialize model.

        **Args**

        device (str): The device to use. Defaults to 'auto'
        **kwargs: Additional arguments to pass to Whisper package
        """
        from mfs_styletts2.lj import LFinference, compute_style
        from openphonemizer import OpenPhonemizer
        import numpy as np
        from scipy.io.wavfile import write
        import torch

        self.torch = torch
        self.np = np
        self.write = write
        self.LFinference = LFinference
        self.compute_style = compute_style
        self.phonemizer = OpenPhonemizer()

    def infer_to_file(
        self,
        text,
        output,
    ):
        sentences = txtsplit(self.phonemizer(text))
        wavs = []
        s_prev = None
        for text in sentences:
            if text.strip() == "":
                continue
            noise = self.torch.randn(1, 1, 256).to('cuda' if self.torch.cuda.is_available() else 'cpu')
            wav, s_prev = self.LFinference(
                text,
                s_prev,
                noise,
                alpha=0.3,
                diffusion_steps=10,
                embedding_scale=1.1,
                phonemize=False
            )
            wavs.append(wav)
        self.write(output, 24000, self.np.concatenate(wavs))
