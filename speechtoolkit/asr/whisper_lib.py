from speechtoolkit.utils.device import device_map


class WhisperModel:
    """
    Use OpenAI Whisper for automatic speech recognition.

    **Args**

    model (str): Which Whisper model to use
    device (str): The device to use. Defaults to 'auto'
    **kwargs: Additional arguments to pass to Whisper package
    """

    def __init__(
        self,
        model="base",
        device="auto",
        **kwargs,
    ):
        """
        Initialize model.

        **Args**

        model (str): Which Whisper model to use
        device (str): The device to use. Defaults to 'auto'
        **kwargs: Additional arguments to pass to Whisper package
        """
        import whisper

        self.model = whisper.load_model(model, **kwargs).to(device_map(device))

    def infer_file(self, audio_path, **kwargs):
        """
        Run inference on a single file.

        **Args**

        audio_path (str): The path of the original audio.
        **kwargs: Additional arguments to pass to Whisper package

        **Returns**

        str: The transcript of the audio file.
        """
        return self.model.transcribe(audio_path, **kwargs)["text"].strip()
