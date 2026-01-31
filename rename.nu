#!/usr/bin/env nu

let course_name = "COL750_2502"

ls *.pdf
| where type == file
| each {|f|
    let parsed = (
        $f.name
        | parse -r 'lec(?<num>\d+)'
    )

    if ($parsed | is-empty) {
        # skip files that don't match
        null
    } else {
        let lec_num = $parsed.num.0
        let new_name = $"($course_name)_Lec($lec_num).pdf"
        mv $f.name $new_name
    }
}
