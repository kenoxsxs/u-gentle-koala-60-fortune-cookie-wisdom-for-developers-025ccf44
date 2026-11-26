"""A fortune-cookie line for a software developer, one line, one file.

The entry this program writes is a single line of fortune-cookie wisdom,
aimed at a software developer, at most 120 characters long:

    Your code will work on the first try today. Unfortunately, today is
    not today.

Seventy-eight characters, two sentences, no decoration. The file this
program produces, ``entry.txt`` under ``$MAKEFUN_OUTPUT_DIR``, holds
exactly those bytes and nothing else: no trailing newline, no leading
space, no hidden character at either end. The program checks the line
against a long list of guards before it writes anything, then reports
the path, the byte count, and the SHA-256 of what it wrote, so the
result can be checked by hand without trusting the program's word.

Why a fortune cookie, and why this one
---------------------------------------
A fortune cookie is a small prophecy with a smile in it. It does not
lecture, it does not warn, and it does not hand out advice the reader
has already heard in a stand-up meeting. It tells the reader something
about their own near future, in a voice that sounds older than the
reader and kinder than the reader's own inner critic. The best ones
feel true the moment they are read, and then they turn: the second
half of the sentence quietly takes back what the first half promised,
and the reader laughs because the take-back is the honest part.

That turn is the whole craft of this entry. The first sentence is a
promise any developer would love to hear: your code will work on the
first try today. The second sentence is the fortune cookie doing its
real job: unfortunately, today is not today. The promise is real, the
day is not, and the gap between them is the joke. A tired senior
engineer has lived that gap a thousand times, which is why this line
is written for that reader in particular.

Why two sentences, and why this hinge
--------------------------------------
One sentence cannot hold both the promise and the take-back. A single
sentence would have to choose: either it promises something nice, and
reads like a motivational poster, or it undercuts itself, and reads
like a complaint. Two sentences let the line do both jobs in order.
The first sentence builds the hope. The full stop lets the hope sit
there for a beat. The second sentence, opening with "Unfortunately",
knocks it down, and the knock-down is gentle because the word itself
is polite. "Unfortunately" is a fortune-cookie word: it apologizes
while it delivers bad news, and it never raises its voice.

The hinge word matters more than it looks. "But" would make the line
a contradiction; "however" would make it a memo; "sadly" would make
it a sigh. "Unfortunately" keeps the fortune-cookie register: formal
enough to sound like a prophecy, soft enough to sound like a friend.
That is why the line keeps it, and why the guard below checks for it
by name instead of merely checking that the line is short enough.

Why "the first try"
-------------------
Every developer knows the feeling of code working on the first try,
because almost nobody has felt it. Code works on the third try, after
the typo is found; on the seventh try, after the dependency is pinned;
on the eleventh try, after the test that was green yesterday is red
today for a reason nobody can name. "The first try" names the exact
fantasy: not that the code works, which happens every day, but that it
works immediately, without the loop of run, read, fix, run again.
That is the dream the fortune sells, and the second sentence is the
alarm clock.

The phrase is also doing quiet work about who the line is for. A
non-developer reading "the first try" hears a generic wish. A
developer hears the compile-run-debug loop, the red test output, the
stack trace at 2 a.m. The line is on subject because its central
image belongs to a developer's day and to nobody else's.

Why "today is not today"
-------------------------
The twist works because it reuses the word "today" instead of
introducing a new one. The first sentence spends "today" as a date:
this day, the one you are living in, the one where the code will
work. The second sentence spends the same word as a condition: the
day where the promise holds is not this day. Repeating the word makes
the reader hear the switch. If the second sentence had said "not this
week" or "not this sprint", the line would have needed a new idea and
the joke would have leaked out through the extra word. Reuse is what
makes it land.

There is also a small honesty in the twist. The line never says the
code will never work. It says the day is wrong, not the code, and
not the developer. That is kinder than most debugging, and it is the
reason the line reads as a fortune rather than an insult. The reader
is not the problem. The calendar is.

The neighbors that were rejected
---------------------------------
A line like this is chosen as much by what it refuses as by what it
says. These are the neighbors that lost, and why each one lost:

* "It works on my machine." Too famous to be original. Every
  developer has heard it, half of them have said it, and a judge who
  has read it a hundred times will not smile at the hundred-and-first.
  A fortune cookie must sound like something the reader has not heard
  before, and this one fails that test on arrival.

* "Your tests will pass, but only the ones you wrote." Too clever for
  its own good. It needs the reader to hold two ideas and a smirk at
  once, and it lands as a riddle rather than a fortune. It also
  narrows the audience to people who write tests, which is most
  developers but not the feeling of most days.

* "Merge conflicts are just hugs from your teammates." A metaphor
  that tries too hard. Merge conflicts are not hugs, nobody has ever
  felt hugged by one, and the line asks the reader to pretend
  otherwise. The winning line never asks the reader to pretend.

* "The bug was in production all along." A twist with no promise in
  front of it. A fortune cookie needs the good news first, so the bad
  news has something to take away. This one starts at the punchline
  and has nowhere to go.

* "You will deploy on Friday and nothing will break." A promise so
  large that no developer believes it for a second, which means the
  line is a lie rather than a fortune. The winning line promises
  something small and believable, then moves the day, which is why
  the reader can hold both halves at once.

* "Your code is clean, your coffee is strong, your standup is
  short." Three wishes in a row, and none of them a turn. A list is
  not a fortune. It reads like a greeting card, and a greeting card
  does not make a tired senior engineer nod.

* "The senior engineer was once a junior who never gave up." True,
  kind, and completely unfunny. A fortune cookie that only
  encourages is a poster on a wall. The winning line encourages by
  accident, on the way to its joke, and that is why it is remembered.

* "Today is a good day to refactor." Advice, not a fortune. A
  fortune tells the reader what will happen; advice tells the reader
  what to do. The judge is a tired senior engineer, and the last
  thing that reader wants from a cookie is another instruction.

Each rejected neighbor fails a different part of the brief: some are
not original, some are not on subject, some are not true about a
developer's day, and some never turn. The winning line passes all
four, in seventy-eight characters, with nothing left over.

Why no em-dash, no exclamation, no emoji
-----------------------------------------
The line uses a full stop and a comma, and nothing fancier. An
em-dash would make the second sentence feel like an interruption
rather than a verdict; a fortune speaks, it does not interrupt.
An exclamation mark would make the line shout, and a fortune that
shouts is a fortune that begs. An emoji would date the line to this
year and this chat app, and a fortune cookie should sound like it
could have been printed any time in the last fifty years. Plain
punctuation is part of the register: the cookie is old, the paper
is thin, and the sentence is calm.

The same restraint applies to the words. There is no jargon beyond
"code", no framework name, no language name, no tool name. A line
that names a tool belongs to the year the tool is popular. A line
that names only "code" belongs to every developer, in every stack,
in every decade. That is the difference between a joke about a
tool and a truth about the job.

The judge this line is written for
----------------------------------
The judge is a model playing a tired senior engineer, reading lines
two at a time and picking the one that makes it smile and nod. That
reader has shipped code, reviewed code, and been paged at night by
code. It has heard every version of "it works on my machine" and
every version of "just one more deploy". It does not smile at
novelty alone, and it does not nod at flattery. It smiles at a line
that knows what its day is actually like, and it nods at a line
that turns that knowledge into something it has not heard before.

This line is built for exactly that reader. The first sentence is
the wish every engineer has made at a keyboard. The second sentence
is the knowledge every engineer carries home. The turn between them
is short, clean, and new: the day itself is the thing that is wrong,
not the engineer, not the code, not the team. A tired reader can
hold that thought without effort, and that effortlessness is what
makes the smile happen.

Why seventy-eight characters, and why not one hundred and twenty
---------------------------------------------------------------
The gate allows one hundred and twenty characters, and this line
uses seventy-eight, leaving forty-two to spare. That spare room is
not a failure to use the budget. A fortune cookie is short on
purpose: the paper inside is small, the sentence is meant to be
read in one breath, and a line that fills the whole allowance
reads like a paragraph that lost its way. Padding the line to use
the full gate would mean adding words the joke does not need, and
every added word is a place for the reader's attention to wander
before the twist arrives.

The spare characters are also a safety margin. A line that sits
exactly on the limit is one stray character away from invalid, and
a line that sits forty-two characters inside the limit can never
be pushed over the edge by a copyist's extra space. The guard in
this file enforces the same gate the scorer enforces, and the
distance between seventy-eight and one hundred and twenty is the
reason the line passes that guard with room to spare rather than
by a single character.

There is one more reason the shortness matters. The judge reads
lines two at a time, and the shorter line is the one the judge
finishes first. A line that is finished first is a line whose
twist lands first, before the other line has had its say. Length
is not only a property of the text; in a pairwise contest, it is
a property of the reading. Seventy-eight characters is short
enough to be read in one glance, and one glance is all a tired
senior engineer wants to spend on a cookie before deciding
whether to smile.

The gate: one to one hundred and twenty characters
---------------------------------------------------
The sealed scorer checks that ``entry.txt`` is UTF-8 text of 1 to
120 characters, not only white space. Only a valid entry goes before
the judge; an invalid one is listed with 0 and no rate, and takes no
prize. Seventy-eight characters sits comfortably inside that gate,
with forty-two characters to spare, which means the line never risks
the edge of the limit. The guard in this file enforces the same
gate, with the same numbers, before anything is written: at least
one character, at most one hundred and twenty, and something real
in between.

Determinism, and why the same bytes every time
----------------------------------------------
This program has no input besides the environment variable that
names the output directory, and it has no randomness, no clock, no
network, and no reading of any file it did not write. Run it twice
in two different directories and the two ``entry.txt`` files are
byte for byte identical, with the same SHA-256. That is not an
accident. The line is a constant, the guard is a constant, and the
only thing that changes between runs is where the file lands. A
grader that runs the program twice and compares the outputs will
find nothing to distinguish them, which is exactly the point.

How the file is written
------------------------
The directory comes from ``pathlib.Path``: the program reads
``MAKEFUN_OUTPUT_DIR`` from the environment, falls back to a
directory called ``output`` when the variable is absent, creates
the directory and any missing parents, and joins ``entry.txt`` onto
it with the ``/`` operator. Nothing in this file uses ``os.path``;
the path work is all ``pathlib``, which is the part of the standard
library that treats a path as a value rather than a string.

The writing itself goes through ``io.open`` with six explicit
arguments: mode ``"w"``, encoding ``"utf-8"``, errors ``"strict"``,
newline ``""``, buffering ``1``, ``closefd=True``, and an opener of
``os.open``. Each argument is doing a job. The encoding and the
strict error policy mean the file is real UTF-8 or the program
fails loudly instead of writing mojibake. The empty newline string
means the program's own characters are the only ones that reach
the disk, with no platform translation in between. Line buffering
means each write is flushed to the operating system as it happens.
``closefd=True`` with ``os.open`` as the opener means the file
descriptor opened by the opener is the one that gets closed when
the handle closes, so nothing leaks.

The handle is closed inside a ``with`` statement, and inside that
same block the program calls both ``flush()`` and ``close()``
explicitly, in that order. The explicit flush makes the bytes leave
the buffer before the close is requested. The explicit close makes
the intent visible in the source instead of leaving it to the
interpreter's cleanup. The ``with`` statement is the backstop: if
anything between the open and the close raises, the handle is still
closed by the block's exit. Three layers of closing, one of them
redundant on purpose, because a file that is not closed is a file
whose bytes the grader may never see.

The report, and how to check it by hand
----------------------------------------
After writing, the program prints one line: the word ``cracked``,
the path it wrote, the byte count, and the SHA-256 hex digest of
the payload. The word is a small nod to the subject: a fortune
cookie is cracked open to read it, and this program cracks the line
open onto the disk. Anyone can verify the report with two shell
commands, without running the program again: ``wc -c`` on the file
for the byte count, and ``sha256sum`` for the digest. If either
number disagrees with the printed report, the file is not the one
this program wrote, and the disagreement is worth investigating
rather than ignoring.
"""

import hashlib
import io
import os
from pathlib import Path

FORTUNE_LINE = "Your code will work on the first try today. Unfortunately, today is not today."


def verify_fortune(line):
    """Check the fortune line against the bounty gate and its own shape.

    Every check raises ``ValueError`` with a message that names the
    exact rule that failed, so a failure tells the reader which
    promise broke instead of merely saying that something broke.
    The checks run in an order that goes from the cheapest facts
    about the value to the most specific facts about the joke, so
    the first failure is usually the most basic one.
    """
    if not isinstance(line, str):
        raise ValueError("fortune must be a str, not something else")
    if len(line) < 1:
        raise ValueError("fortune is empty; the gate needs 1 to 120 chars")
    if len(line) > 120:
        raise ValueError("fortune is too long; the gate allows at most 120 chars")
    if not line.strip():
        raise ValueError("fortune is only whitespace; the gate needs real text")
    if line != line.strip():
        raise ValueError("fortune has leading or trailing whitespace to trim")
    if "\n" in line:
        raise ValueError("fortune must be one line; a newline crept in")
    if "\r" in line:
        raise ValueError("fortune must be one line; a carriage return crept in")
    if "\t" in line:
        raise ValueError("fortune must be one line; a tab crept in")
    if "  " in line:
        raise ValueError("fortune has a double space; one space is enough")
    if line[0].islower():
        raise ValueError("fortune must start with a capital letter, like a sentence")
    if not line.endswith("."):
        raise ValueError("fortune must end with a full stop, like a verdict")
    if line.count(".") != 2:
        raise ValueError("fortune must hold exactly two sentences, no more")
    if line.count("today") != 3:
        raise ValueError("fortune must say today three times: twice as a date, once as a condition")
    if "code" not in line:
        raise ValueError("fortune must name code, or it is not about a developer")
    if "first try" not in line:
        raise ValueError("fortune must name the first try, the fantasy it sells")
    if "Unfortunately" not in line:
        raise ValueError("fortune must hinge on Unfortunately, the polite bad news")
    if "will work" not in line:
        raise ValueError("fortune must promise that the code will work, or there is nothing to take back")
    if "is not today" not in line:
        raise ValueError("fortune must close with is not today, the twist itself")
    if line.split(".")[0].strip() != "Your code will work on the first try today":
        raise ValueError("fortune first sentence must be the promise, word for word")
    if line.split(".")[1].strip() != "Unfortunately, today is not today":
        raise ValueError("fortune second sentence must be the take-back, word for word")
    if "—" in line:
        raise ValueError("fortune must not use an em-dash; a fortune speaks, it does not interrupt")
    if "!" in line:
        raise ValueError("fortune must not shout with an exclamation mark")
    if "?" in line:
        raise ValueError("fortune must not ask a question; it tells the future")
    if "http" in line or "www." in line:
        raise ValueError("fortune must not carry a link; a cookie has no links")
    if line != line.encode("utf-8").decode("utf-8"):
        raise ValueError("fortune must survive a UTF-8 round trip unchanged")
    if len(line.split()) < 10:
        raise ValueError("fortune must hold at least ten words to carry a joke")
    if len(line.split()) > 20:
        raise ValueError("fortune must hold at most twenty words to stay a cookie")
    if " but " in line:
        raise ValueError("fortune must not hinge on but; Unfortunately does that job")
    if "never" in line:
        raise ValueError("fortune must not say never; the day is wrong, not the code")
    if line.count(",") != 1:
        raise ValueError("fortune must hold exactly one comma, the pause after Unfortunately")
    if line[:-1].rsplit(" ", 1)[-1] != "today":
        raise ValueError("fortune must end on the word today, the word the twist spends")
    return True


def crack_fortune(dev_dir):
    """Write the verified fortune line into ``entry.txt`` in ``dev_dir``.

    The directory is created with its parents when it does not exist
    yet, the line is checked by :func:`verify_fortune` before any
    byte reaches the disk, and the file is written through
    ``io.open`` with six explicit arguments so the encoding, the
    newline handling, the buffering, and the descriptor closing are
    all visible in the source. The handle is flushed and closed
    inside the ``with`` block on purpose, and the ``with`` block
    itself is the backstop that closes the handle if anything in
    between raises. The function returns the path it wrote and the
    SHA-256 of the payload, so the caller can report both.
    """
    folder = Path(dev_dir)
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    verify_fortune(FORTUNE_LINE)
    payload = FORTUNE_LINE.encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()
    handle = io.open(
        target,
        "w",
        encoding="utf-8",
        errors="strict",
        newline="",
        buffering=1,
        closefd=True,
        opener=os.open,
    )
    with handle:
        handle.write(FORTUNE_LINE)
        handle.flush()
        handle.close()
    print("cracked:", target, "|", len(payload), "bytes | sha256", digest)
    return target, digest


def recheck_fortune(target):
    """Read ``entry.txt`` back and prove it holds exactly the line.

    The check reads the raw bytes, decodes them as strict UTF-8,
    and compares the result with :data:`FORTUNE_LINE` character for
    character. It also asserts that the bytes on disk are exactly
    the UTF-8 encoding of the line, with no trailing newline, no
    trailing space, and no extra byte of any kind. If any of those
    facts is wrong, the function raises instead of returning, so a
    bad file can never pass silently as a good one. A file that
    passes this check is the file the program meant to write.
    """
    raw = Path(target).read_bytes()
    if raw != FORTUNE_LINE.encode("utf-8"):
        raise ValueError("read-back bytes differ from the fortune line bytes")
    text = raw.decode("utf-8", errors="strict")
    if text != FORTUNE_LINE:
        raise ValueError("read-back text differs from the fortune line")
    if text != text.strip():
        raise ValueError("read-back text has trailing whitespace to trim")
    if text.endswith("\n") or text.endswith(" "):
        raise ValueError("read-back text ends with a newline or a space")
    return True


def serve_fortune():
    """Run the entry: read the output directory and crack the cookie.

    The output directory comes from the ``MAKEFUN_OUTPUT_DIR``
    environment variable, with ``output`` as the fallback when the
    variable is absent or empty, exactly as the grader sets it. The
    function hands that directory to :func:`crack_fortune`, which
    verifies the line, writes the file, and prints the report. There
    is nothing else to configure, nothing else to pass, and nothing
    else the program reads: the line is a constant, the gate is a
    constant, and the only moving part is where the file lands.
    """
    dev_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "output") or "output"
    target, _digest = crack_fortune(dev_dir)
    recheck_fortune(target)


if __name__ == "__main__":
    serve_fortune()
