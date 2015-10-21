# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""To MARC 21 model definition."""

from dojson import utils

from ..model import to_marc21


@to_marc21.over('210', '^abbreviated_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_abbreviated_title(self, key, value):
    """Reverse - Abbreviated Title."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {
        "Abbreviated key title": "_",
        "Other abbreviated title": "0"}
    return {
        'a': value.get('abbreviated_title'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '2': utils.reverse_force_list(
            value.get('source')
        ),
        'b': value.get('qualifying_information'),
        '6': value.get('linkage'),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), '_'),
        '$ind2': indicator_map2.get(value.get('type'), '_'),
    }


@to_marc21.over('222', '^key_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_key_title(self, key, value):
    """Reverse - Key Title."""
    indicator_map2 = {
        "No nonfiling characters": "0",
        "Number of nonfiling characters": "8"}
    return {
        'a': value.get('key_title'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        'b': value.get('qualifying_information'),
        '6': value.get('linkage'),
        '$ind1': '_',
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21.over('240', '^uniform_title$')
@utils.filter_values
def reverse_uniform_title(self, key, value):
    """Reverse - Uniform Title."""
    indicator_map1 = {
        "Not printed or displayed": "0",
        "Printed or displayed": "1"}
    indicator_map2 = {"Number of nonfiling characters": "8"}
    return {
        'a': value.get('uniform_title'),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_of_a_work'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')),
        'l': value.get('language_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')),
        '0': utils.reverse_force_list(
            value.get('authority_record_control_number')),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('uniform_title_printed_or_displayed'),
            '_'),
        '$ind2': indicator_map2.get(
            value.get('nonfiling_characters'),
            '_'),
    }


@to_marc21.over('242', '^translation_of_title_by_cataloging_agency$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_translation_of_title_by_cataloging_agency(self, key, value):
    """Reverse - Translation of Title by Cataloging Agency."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {
        "No nonfiling characters": "0",
        "Number of nonfiling characters": "8"}
    return {
        'a': value.get('title'),
        'c': value.get('statement_of_responsibility'),
        'b': value.get('remainder_of_title'),
        'h': value.get('medium'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        'y': value.get('language_code_of_translated_title'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21.over('243', '^collective_uniform_title$')
@utils.filter_values
def reverse_collective_uniform_title(self, key, value):
    """Reverse - Collective Uniform Title."""
    indicator_map1 = {
        "Not printed or displayed": "0",
        "Printed or displayed": "1"}
    indicator_map2 = {"Number of nonfiling characters": "8"}
    return {
        'a': value.get('uniform_title'),
        'd': utils.reverse_force_list(
            value.get('date_of_treaty_signing')),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_of_a_work'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form_subheading')),
        'm': utils.reverse_force_list(
            value.get('medium_of_performance_for_music')),
        'l': value.get('language_of_a_work'),
        'o': value.get('arranged_statement_for_music'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')),
        's': value.get('version'),
        'r': value.get('key_for_music'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('uniform_title_printed_or_displayed'),
            '_'),
        '$ind2': indicator_map2.get(
            value.get('nonfiling_characters'),
            '_'),
    }


@to_marc21.over('245', '^title_statement$')
@utils.filter_values
def reverse_title_statement(self, key, value):
    """Reverse - Title Statement."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {
        "No nonfiling characters": "0",
        "Number of nonfiling characters": "8"}
    return {
        'a': value.get('title'),
        'c': value.get('statement_of_responsibility'),
        'b': value.get('remainder_of_title'),
        'g': value.get('bulk_dates'),
        'f': value.get('inclusive_dates'),
        'h': value.get('medium'),
        'k': utils.reverse_force_list(
            value.get('form')
        ),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        's': value.get('version'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), '_'),
        '$ind2': indicator_map2.get(value.get('nonfiling_characters'), '_'),
    }


@to_marc21.over('246', '^varying_form_of_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_varying_form_of_title(self, key, value):
    """Reverse - Varying Form of Title."""
    indicator_map1 = {
        "No note, added entry": "3",
        "No note, no added entry": "2",
        "Note, added entry": "1",
        "Note, no added entry": "0"}
    indicator_map2 = {
        "Added title page title": "5",
        "Caption title": "6",
        "Cover title": "4",
        "Distinctive title": "2",
        "No type specified": "_",
        "Other title": "3",
        "Parallel title": "1",
        "Portion of title": "0",
        "Running title": "7",
        "Spine title": "8"}
    return {
        'a': value.get('title_proper_short_title'),
        'b': value.get('remainder_of_title'),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_or_sequential_designation'),
        'i': value.get('display_text'),
        'h': value.get('medium'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')),
        '5': value.get('institution_to_which_field_applies'),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')),
        '$ind1': indicator_map1.get(
            value.get('note_added_entry_controller'),
            '_'),
        '$ind2': indicator_map2.get(
            value.get('type_of_title'),
            '_'),
    }


@to_marc21.over('247', '^former_title$')
@utils.reverse_for_each_value
@utils.filter_values
def reverse_former_title(self, key, value):
    """Reverse - Former Title."""
    indicator_map1 = {"Added entry": "1", "No added entry": "0"}
    indicator_map2 = {"Display note": "0", "Do not display note": "1"}
    return {
        'a': value.get('title'),
        'x': value.get('international_standard_serial_number'),
        'b': value.get('remainder_of_title'),
        'g': value.get('miscellaneous_information'),
        'f': value.get('date_or_sequential_designation'),
        'h': value.get('medium'),
        'n': utils.reverse_force_list(
            value.get('number_of_part_section_of_a_work')
        ),
        'p': utils.reverse_force_list(
            value.get('name_of_part_section_of_a_work')
        ),
        '6': value.get('linkage'),
        '8': utils.reverse_force_list(
            value.get('field_link_and_sequence_number')
        ),
        '$ind1': indicator_map1.get(value.get('title_added_entry'), '_'),
        '$ind2': indicator_map2.get(value.get('note_controller'), '_'),
    }