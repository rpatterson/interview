===============================
Density API Homework Assignment
===============================

I'm delaying DB or other prod scaling consideration at first.  I'll
start with the Django default DB, sqlite, until other features are
needed.

Per "don't worry about best-practices", I'm starting with a too
monolithic integration test for expediency over long-term
maintainability, something I wouldn't do otherwise.  Per "with app
structure", I'm putting everything in the Django project level when
one really should create a Django app for this kind of code and the
project should only be used to tie everything together.

I'm beginning with a test describing the models and their
relationships.

I'm thinking about the "DPUs are sometimes moved from one doorway to
another" and how to model that.  I'd guess that it's not important
which *specifi* DPU took a measurement, just which specific doorway it
was on.  For now, however, I'm going to go ahead and keep both
relationships in the DB.  This is almost certainly a scalability
issue, but I'm erring on the side of not optimizing prematurely.

Might as well model the given diagram in the test.

Hmm, how to model directionality?  Doorways have a relationship with
1-2 spaces.  Maybe that can be used to establish part of
directionality.  Perhaps we can say "This door goes *into* this space,
and *out of* that space.  That may not always be true, some set of
spaces may be peers in some sense where in vs out is arbitrary but I
can't, ATM, think of any problem with that.  So going with in vs out
spaces for doorways for now.

So now we have doorway directionality, now we need to relate the DPU's
directionality to the doorway directionality.

To clarify, from the diagram, it looks like the DPU directionality may
not match the doorway directionality.  IOW, a +1 measurement could
correspond to going into or out of a room.  So we need both doorway
directionality to model the relationships between spaces, and then DPU
directionality in relation to doorway directionality to translate
+1/-1 measurements to entering or leaving spaces.  So we'll record
relationships between DPUs and spaces as plus and minus spaces where
either of those may be empty.  It should be an error for *both* of
them to be empty. 

I dislike Django fixtures, I've found them too fragile, result in
noisy/unreadable diffs in VCS, and make it too difficult for a
developer to understand the intention of the fixtures.  So I'm going
to abuse a Django data DB migration to set up the fixture we need for
both tests and to demo the API.  I don't mind working with fixtures
when the team uses them, it's just a slight personal preference.

Allowing space names be quite long for now.  Should be revisited.

We can't assume that a doorway should be deleted if the space is
deleted because it may be connected to another space, but it should
also be an error to leave a doorway with neither a in or out space.
Ditto for DPUs. Punting for now.

Looking at the CSV, it includes only DPU, not doorway.  This seems to
contradict "DPUs are sometimes moved from one doorway to another".
I'm assuming that the measurements will be associated with the
doorways per the diagram.

Should deleting a doorway delete the measurements?  A measurement
without a doorway seems meaningless.  Punting for now.

I'm beginning to suspect that the way I'm modeling doorway and DPU
directionality may be redundant in terms of the minimum required to
interpret the measurements.  I'm going to leave it as is for the
moment since the relationships still do reflect "reality".

I'm assuming that a "count" means the number of passes in either
direction over a given time period.  You can't get the realtime or
historical number of people in a room without some way to know when
the space was last empty, and given that there may be holes in the
data that doesn't seem feasible.  So i'm not sure what "realtime"
means.  For now, I'll assume "realtime" just means a period of time in
relation to now, IOW, the last hour or last day.

Oh wait, we have to record the directionality of the DPU at the time
we record a measurement.  Rethinking the schema.
