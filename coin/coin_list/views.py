from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf.urls import url


def quarter_list(request):

    return render(request, 'coin_list/coin.html')
