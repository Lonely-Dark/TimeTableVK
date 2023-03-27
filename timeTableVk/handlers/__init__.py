#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.11

from . import menu, back_action, important, five_classes, six_classes, seven_classes, eight_classes, nine_classes, \
    ten_classes, eleven_classes, extension, timetable_calls, all_timetable

labelers = [menu.menu_labeler, back_action.back_labeler, important.important_labeler, five_classes.five_labeler,
            six_classes.six_labeler, seven_classes.seven_labeler, eight_classes.eight_labeler,
            nine_classes.nine_labeler, ten_classes.ten_labeler, eleven_classes.eleven_labeler,
            extension.extension_labeler, timetable_calls.calls_labeler, all_timetable.timetables_all_labeler]

__all__ = ["labelers"]
