===========================================
Assigmnent Notes
===========================================
Stream-of-consciousness notes of my process
-------------------------------------------

Firstly, I copied the samples from the assignment into text files and
wired up a failing test that takes the input and checks the output
against the expected output.

Looking at the paragraph, questions, and answers, there's no simple
way, such as taking the N last words, to find the relevant portion of
the question to search for in the paragraph.  That would be a bad idea
anyways as it would be very fragile and very likely to fail for other
input.  At it's core, this is a natural language processing (NLP)
problem so according to the principle of re-use, I went searching for
a good NLP library to use for this problem.  I'm not an NLP expert, so
if you intended me to implement something from scratch can you provide
additional direction as to how to put bounds on the solution.  IOW,
how to *not* end up reimplementing an existing NLP library.

In the meantime, without teaching myself NLP more in depth, I opted
for matching questions to the corresponding sentence in the paragraph
based on the largest intersection of normalized words in common.  As I
didn't end up using much of the NLP library, it might be worth it to
remove that dependency if this were intended for actual use.
