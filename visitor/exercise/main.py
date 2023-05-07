from .wav_file import WavFile
from .fact_segment import FactSegment
from .format_segment import FormatSegment
from .reduce_noise_filter import ReduceNoiseFilter
from .reverb_filter import ReverbFilter
from .normalize_filter import NormalizeFilter

if __name__ == '__main__':
    document = WavFile()
    document.add(FactSegment())
    document.add(FormatSegment())
    document.execute(ReduceNoiseFilter())
    document.execute(ReverbFilter())
    document.execute(NormalizeFilter())
