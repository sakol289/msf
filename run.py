ó
ac           @   s^  d  d l  Z  d  d l Z d  d l m Z d  d l Z e  j d  e  j d  e j d  e  j d  d   Z e  j d  d Z e e  e e d   Z	 e	 d k r¼ e  j d	  n e	 d
 k rå e  j d  e  j d  nu e	 d k re  j d  nY e	 d k re  j d  n= e	 d k r9e  j d  n! e	 d k rUe  j d  n d GHd S(   iÿÿÿÿN(   t   sleept   clears+   cd /$HOME/msf/system;python3 progressbar.pyi   c         C   sG   x@ |  d D]4 } t  j j |  t  j j   t j d d  q Wd  S(   Ns   
g       @iZ   (   t   syst   stdoutt   writet   flusht   timeR    (   t   st   c(    (    s   run.pyt
   slowprints   s    sU  [1;33;40m
********************************
*                              *
*            1 setup           *
*            2 console         *
*            3 update          *
*            4 cr              *
*            5 ngrok           *
*           00 exit            *
*                              *
********************************
s   Press enter to continue...:s4   clear;cd /$HOME/msf/system/setup;python3 runsetup.pyi   s2   cd /$HOME/msf/system/console;python3 runconsole.pyi   s)   git pull https://github.com/sakol289/msf/i   s   clear;cd system;python3 cr.pyi   s4   clear;cd /$HOME/msf/system/ngrok;python3 runngrok.pyi    t   exits   vkg0 ld] Tkouiy9oN(
   t   osR   R   R    t   systemR	   t   semutt   intt   inputt   x(    (    (    s   run.pyt   <module>   s2   	
