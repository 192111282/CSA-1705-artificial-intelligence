% Facts: Names and Dates of Birth
dob(vijay, '2004-05-15').
dob(toufiq, '2003-12-10').
dob(sheshaa, '2003-03-22').
dob(siddu, '2006-08-28').

% Queries
% Find the DOB of a person
dob(Name, DOB) :-
    name(Name, DOB).