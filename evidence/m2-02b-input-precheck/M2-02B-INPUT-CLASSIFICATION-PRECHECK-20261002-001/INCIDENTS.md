# Precheck harness incident

The initial batch command exceeded the container execution timeout after completing ffprobe for Slow_70mm_4K120fps.MP4 and its 10% preview. This is a harness timeout, not a media failure. No completed outputs were overwritten. Only the remaining 25/50/75/90% preview extractions and contact-sheet assembly were continued in a targeted command.

The Slow_70mm 10% preview was then rerun to obtain an explicit exit status. The replay was byte-identical to the already completed pre-timeout preview.

All recorded ffprobe/preview command statuses used by the precheck are zero.
