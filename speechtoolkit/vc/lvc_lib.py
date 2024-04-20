class LVCModel:
    """
    Use LVC-VC (End-to-End Zero-Shot Voice Conversion with Location-Variable Convolutions) for zero-shot voice conversion.

    **Args**

    device (str): The device to use. Defaults to 'auto'
    use_xl_model (bool): Use the XL model vs. the smaller model. Defaults to 'true'
    **kwargs: Additional arguments to pass to package
    """

    def __init__(
        self,
        device="auto",
        use_xl_model=True,
        **kwargs,
    ):
        """
        Initialize model.

        **Args**

        device (str): The device to use. Defaults to 'auto'
        use_xl_model (bool): Use the XL model vs. the smaller model. Defaults to 'true'
        **kwargs: Additional arguments to pass to package
        """
        from lvc import LVC

        self.model = LVC(device=device, use_xl_model=use_xl_model, **kwargs)

    def infer_file(
        self, original_audio_path, sample_audio_path, output_audio_path, **kwargs
    ):
        """
        Run inference on a single file.

        **Args**

        original_audio_path (str): The path of the original audio.
        sample_audio_path (str): The path of the speaker sample whose voice you want to clone.
        output_audio_path (str): The path to save your audio
        """
        self.model.infer_file(
            original_audio_path, sample_audio_path, output_audio_path, **kwargs
        )
