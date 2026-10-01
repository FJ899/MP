# M2-01 Execution Incidents

Three execution-harness incidents were preserved and excluded from the clean formal evidence set:

1. A shell wrapper failed while capturing PIPESTATUS because the array was read after an intervening assignment under set -u. No media failure was inferred.
2. An early while-read wrapper exposed the sample TSV on stdin; FFmpeg's interactive stdin handling consumed bytes from the next row. Partial extraction evidence was discarded. The formal restart used -nostdin plus an in-memory sample list.
3. The container execution harness timed out after formal Run A and formal Run B p10 had completed. Those completed commands had exit status 0. Remaining independent Run B samples p30/p50/p70/p90 were continued without repeating completed samples.

The PASS result is based only on statuses_formal.txt and the final comparison set. Every formal command status is 0.
