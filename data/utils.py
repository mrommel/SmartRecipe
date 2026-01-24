import sys

from tqdm import tqdm
from chunkator import chunkator


def red_chunked_bar(qs, total: int, desc: str, chunk_size: int = 10_000):
	tqdm.format_sizeof = lambda x, divisor=None: f"{x:,}" if divisor else f"{x:5.2f}"
	return tqdm(chunkator(qs, chunk_size), total=total, desc=desc, ncols=120, unit_scale=True, colour='red',
	            file=sys.stdout)


def green_chunked_bar(qs, total: int, desc: str, chunk_size: int = 10_000):
	tqdm.format_sizeof = lambda x, divisor=None: f"{x:,}" if divisor else f"{x:5.2f}"
	return tqdm(chunkator(qs, chunk_size), total=total, desc=desc, ncols=120, unit_scale=True, colour='green',
	            file=sys.stdout)


def green_bar(qs, total: int, desc: str):
	tqdm.format_sizeof = lambda x, divisor=None: f"{x:,}" if divisor else f"{x:5.2f}"
	return tqdm(qs, total=total, desc=desc, ncols=120, unit_scale=True, colour='green', file=sys.stdout)


def blue_chunked_bar(qs, total: int, desc: str, chunk_size: int = 10_000):
	tqdm.format_sizeof = lambda x, divisor=None: f"{x:,}" if divisor else f"{x:5.2f}"
	return tqdm(chunkator(qs, chunk_size), total=total, desc=desc, ncols=120, unit_scale=True, colour='blue',
	            file=sys.stdout)


def blue_bar(qs, total: int, desc: str):
	tqdm.format_sizeof = lambda x, divisor=None: f"{x:,}" if divisor else f"{x:5.2f}"
	return tqdm(qs, total=total, desc=desc, ncols=120, unit_scale=True, colour='blue', file=sys.stdout)


def yellow_chunked_bar(qs, total: int, desc: str, chunk_size: int = 10_000):
	tqdm.format_sizeof = lambda x, divisor=None: f"{x:,}" if divisor else f"{x:5.2f}"
	return tqdm(chunkator(qs, chunk_size), total=total, desc=desc, ncols=120, unit_scale=True, colour='yellow',
	            file=sys.stdout)


def magenta_chunked_bar(qs, total: int, desc: str, chunk_size: int = 10000):
	tqdm.format_sizeof = lambda x, divisor=None: f"{x:,}" if divisor else f"{x:5.2f}"
	return tqdm(chunkator(qs, chunk_size), total=total, desc=desc, ncols=120, unit_scale=True, colour='magenta',
	            file=sys.stdout)
