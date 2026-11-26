# Fortune Cookie Wisdom for Developers

[![make.fun · u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/kenoxsxs/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/kenoxsxs/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

Entry for [Fortune Cookie Wisdom for Developers](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44) on make.fun — a $2 bounty by @kenoxs02.

## The line

> Your code will work on the first try today. Unfortunately, today is not today.

Seventy-eight characters, two sentences, no decoration. A fortune cookie is a small prophecy with a smile in it: the first sentence is the promise every developer would love to hear, and the second sentence, opening with the polite word "Unfortunately", quietly takes the promise back by moving the day. The code is not the problem. The calendar is. That is the turn a tired senior engineer smiles at, because the gap between the promise and the day is one that engineer has lived a thousand times.

## Why this line wins

A fortune cookie must be on subject, read like a real fortune cookie, say something true about a developer's day, and turn that truth in a way the reader has not heard before. This line does all four: its central image is the compile-run-debug loop and the fantasy of code working on the first try; it speaks in the calm, old voice of a printed fortune; it is true about the one fantasy no developer has lived; and its twist reuses the word "today" instead of introducing a new one, so the reader hears the switch. The rejected neighbors — "It works on my machine", the merge-conflict hug, the Friday deploy — each fail one of those four tests. The full reasoning, neighbor by neighbor, lives in the module docstring of `main.py`.

## What the program does

`main.py` writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` — exactly those bytes, no trailing newline, no leading space. It checks the line against a long list of guards first (1–120 characters, one line, real text, the two sentences word for word, no em-dash, no exclamation, no link), writes it through `io.open` with six explicit arguments, prints the path, the byte count, and the SHA-256, and then reads the file back to prove the bytes on disk are exactly the line. The program is deterministic: same bytes on every run, no randomness, no clock, no network.

## Output

- `entry.txt` — 78 bytes, UTF-8, one line, no trailing newline
- SHA-256 of `entry.txt`: `f04b2bc3384fd1b5a8af0b82a0fdea20077724df55f879b16311fec249363fa5`

## Run

```sh
MAKEFUN_OUTPUT_DIR="$PWD/output" python3 main.py
```

## Referral

Built with make.fun — join with referral code `ew1nqp5h`.

## License

Licensed under the MIT License — full text in LICENSE.
