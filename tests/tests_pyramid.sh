#!/usr/bin/env bash
readonly SCRIPT_DIRECTORY=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd);
readonly APP_DIRECTORY=${SCRIPT_DIRECTORY}/..

function main
{
    echo "[*] Measure tests pyramid for dsin2 repository.";

    set -o errexit
    set -o pipefail
    set -o nounset
    set -o errtrace

    PS1=${PS1:-}
    measure_tests_pyramid;
}

function measure_tests_pyramid
{
    readonly number_of_unit_tests=$(count_tests test_unit "def test_");
    readonly number_of_int_tests=$(count_tests test_integration "def test_");
    readonly number_of_func_tests=$(count_tests test_functional "Scenario:");
    readonly total_number_of_tests=$(($number_of_unit_tests + $number_of_int_tests + $number_of_func_tests));

    readonly percentage_of_unit_tests=$(percentage ${number_of_unit_tests} ${total_number_of_tests})
    readonly percentage_of_int_tests=$(percentage ${number_of_int_tests} ${total_number_of_tests})
    readonly percentage_of_func_tests=$(percentage ${number_of_func_tests} ${total_number_of_tests})

    echo "
          /\\.           [*] func tests: $number_of_func_tests/$total_number_of_tests --> $percentage_of_func_tests%
         /|_\\\`.
        /__|_\\/\`.
       /__|__|\\/.\`.     [*] int tests: $number_of_int_tests/$total_number_of_tests --> $percentage_of_int_tests%
      /_|__|__|\\/\`/\`.
     /|__|___|__\\/\`/
    /__|___|___|_\\/     [*] unit tests: $number_of_unit_tests/$total_number_of_tests --> $percentage_of_unit_tests%
    ";

    check_if_pyramid_is_ok number_of_unit_tests number_of_int_tests number_of_func_tests
}

function check_if_pyramid_is_ok
{
    readonly nb_unit_tests=${1}
    readonly nb_int_tests=${2}
    readonly nb_func_tests=${3}

    if [[ ${nb_func_tests} -gt ${nb_int_tests} ]] ||
       [[ ${nb_func_tests} -gt ${nb_unit_tests} ]] ||
       [[ ${nb_int_tests} -gt ${nb_unit_tests} ]]; then
          echo "Warning: tests pyramid is unbalanced";
          exit 1;
    fi
}

function percentage
{
    readonly number_of_tests=${1}
    readonly total=${2}

    calc 100*${number_of_tests}/${total}
}

function calc
{
    awk "BEGIN { print $* }";
}

function count_tests
{
    readonly tests_folder=${1}
    readonly pattern_for_one_test=${2}

    find ${APP_DIRECTORY}/tests/${tests_folder}/ -type f -exec grep -e "${pattern_for_one_test}" "{}" \; | wc -l;
}

main
