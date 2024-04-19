from speechtoolkit.vc.model import VCModel

class LVCModel:
    def __init__(self, device = 'auto', **kwargs,):
        from lvc import LVC
        self.model = LVC(device=device, **kwargs)
    def infer_file(
        self,
        original_audio_path,
        sample_audio_path,
        output_audio_path,
        **kwargs
    ):
        self.model.infer_file(
            original_audio_path,
            sample_audio_path,
            output_audio_path,
            **kwargs
        )