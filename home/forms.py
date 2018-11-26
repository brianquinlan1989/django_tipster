from django import forms

class DayOneSelection(forms.Form):

    race_one = forms.CharField(label="Supreme Novices' Hurdle", required=False)
    race_two = forms.CharField(label="Arkle Novices' Chase", required=False)
    race_three = forms.CharField(label="Ultima Handicap Chase", required=False)
    race_four = forms.CharField(label="Champion Hurdle", required=False)
    race_five = forms.CharField(label="Mares' Hurdle", required=False)
    race_six = forms.CharField(label="National Hunt Novices's Chase' Hurdle", required=False)
    race_seven = forms.CharField(label="Novices' Handicap Chase", required=False)