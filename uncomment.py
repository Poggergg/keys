def fix_errors(withings_table):
    the_errors: the_errors = find_errors(withings_table)

    table: adr_row = withings_table[0]

    with table.edit() as editor:
        v = bmi(log(withings_table[the_errors[0][0]]), withings_table[the_errors[0][0]].weight_kg())
        editor[the_errors[0][1]] = v

        for error in the_errors[1:]:
            still_equal: bool = has_factor(factor=3)(
                l=log(withings_table[the_errors[0][0]]),
                any_l=log(withings_table[error[0]]))
            if still_equal:
                v = bmi(log(withings_table[the_errors[0][0]]), withings_table[the_errors[0][0]].weight_kg())
                editor[error[1]] = v

            else:

          if len(the_errors) == 1:
            v = bmi(log(withings_table[the_errors[0][0]]), withings_table[the_errors[0][0]].weight_kg())
            with withings_table.edit()as editor:
                editor[the_errors[0][1]] = v
        else:
            v = bmi(log(withings_table[the_errors[0][0]]), withings_table[the_errors[0][0]].weight_kg())
            print(v)
            with withings_table.edit() as editor:
                editor[the_errors[0][1]] = v



withings_table: adr_table = adr_table("withings")


withings_table = adr_table("withings", key="1595661671210_1000002")
fix_errors(withings_table)

withings_table = adr_table("withings", key="1595661671210_999999")
fix_errors(withings_table)

with withings_table.edit_key("1595661671210_999999") as editor:
    editor[274] = 60400

the_errors = find_errors(withings_table)
table: adr_row = withings_table[0]

# the_errors