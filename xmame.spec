Summary:	Unix/X11 port of M.A.M.E. - arcade machine emulator
Summary(pl):	Port emulatora M.A.M.E. dzia³aj±cy w ¶rodowisku Unix/X11
Name:		xmame
Version:	0.60.1	
Release:	0.1
License:	GPL
Group:		Applications/Emulators
Source0:	%{name}-%{version}.tar.bz2
Source1:        %{name}.png
Source2:	%{name}-SDL.desktop
Source3:	%{name}-x11.desktop

URL:		http://x.mame.net
BuildRequires:	alsa-driver-devel XFree86-devel zlib-devel
#Requires:	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man

%description
X-Mame the UNIX/X11 port of Mame project.
It makes Mame arcade emulator available on *ix machines using the
X11R6 X-Window system (and Linux ones using SVGAlib too).

Mame is a virtual machine emulator: it includes a Z80, 6502, 68000 and
lastly I86 uP emulators, joined to several arcade machine hardware 
emulators. Each arcade emulator contains a full description about
hardware, mem maps, video, sounds and so, making possible that if
you have original ROM images of a supported arcade game, you can
play the game.

%description -l pl
Port emulatora M.A.M.E. dzia³aj±cy w ¶rodowisku Unix/X11.


%package common
Summary:        Xmame - common files
Summary(pl):	Xmame - wspólne pliki
Group:          Applications/Emulators
Requires:       xmame
#Requires:       
#BuildRequires:  

%description common
X-Mame the UNIX/X11 port of Mame project.
It makes Mame arcade emulator available on *ix machines using the
X11R6 X-Window system (and Linux ones using SVGAlib too).

Mame is a virtual machine emulator: it includes a Z80, 6502, 68000 and
lastly I86 uP emulators, joined to several arcade machine hardware 
emulators. Each arcade emulator contains a full description about
hardware, mem maps, video, sounds and so, making possible that if
you have original ROM images of a supported arcade game, you can
play the game.

This package contains base xmame files, reqiuired or not to run xmame. ;)

%description common -l pl
...

%package SDL
Summary:	Xmame with SDL graphic output
Summary(pl):	Xmame z wyj¶ciem graficznym SDL
Group:          Applications/Emulators
Provides:	%{name}
Requires: 	SDL 
BuildRequires:	SDL-devel

%description SDL
X-Mame the UNIX/X11 port of Mame project.
It makes Mame arcade emulator available on *ix machines using the
X11R6 X-Window system (and Linux ones using SVGAlib too).

Mame is a virtual machine emulator: it includes a Z80, 6502, 68000 and
lastly I86 uP emulators, joined to several arcade machine hardware
emulators. Each arcade emulator contains a full description about
hardware, mem maps, video, sounds and so, making possible that if
you have original ROM images of a supported arcade game, you can
play the game.

This package has xmame binaries compiled for SDL graphics output.

%description SDL -l pl
Port emulatora M.A.M.E. dzia³aj±cy w ¶rodowisku Unix/X11.
Ta wersja u¿ywa bibliotek SDL dla wyj¶cia graficznego.

%package svgalib
Summary:        xmame - svgalib version
Summary(pl):    xmame - wersja z wyj¶ciem svgalib
Group:          Applications/Emulators
Provides:       %{name}
Requires:       svgalib
BuildRequires:  svgalib-devel

%description svgalib
X-Mame the UNIX/X11 port of Mame project.
It makes Mame arcade emulator available on *ix machines using the
X11R6 X-Window system (and Linux ones using SVGAlib too).

Mame is a virtual machine emulator: it includes a Z80, 6502, 68000 and
lastly I86 uP emulators, joined to several arcade machine hardware
emulators. Each arcade emulator contains a full description about
hardware, mem maps, video, sounds and so, making possible that if
you have original ROM images of a supported arcade game, you can
play the game.

This package has xmame binaries compiled for svgalib graphic output.

%description svgalib -l pl
...

%package x11 
Summary:        xmame - x11 version
Summary(pl):    xmame - wersja z wyj¶ciem x11
Group:          Applications/Emulators
Provides:       %{name}
Requires:       XFree86-libs
#BuildRequires:  

%description x11
X-Mame the UNIX/X11 port of Mame project.
It makes Mame arcade emulator available on *ix machines using the
X11R6 X-Window system (and Linux ones using SVGAlib too).

Mame is a virtual machine emulator: it includes a Z80, 6502, 68000 and
lastly I86 uP emulators, joined to several arcade machine hardware
emulators. Each arcade emulator contains a full description about
hardware, mem maps, video, sounds and so, making possible that if
you have original ROM images of a supported arcade game, you can
play the game.

This package has xmame binaries compiled for x11 graphic output.

%description x11 -l pl
...

%package screensaver
Summary:        xmame - screensaver
Summary(pl):    xmame - wygaszacz ekranu
Group:          Applications/Emulators
Requires:       XFree86-libs
#BuildRequires:  

%description screensaver
The xmame screensaver. ;)

%description x11 -l pl
Wygaszacz ekranu xmame.

%prep

%setup -q
#%patch0 -p1

%build

%{__make} -f makefile.unix \
PREFIX=%{_prefix} XMAMEROOT=$RPM_BUILD_ROOT%{_datadir}/games/%{name}
CC="%{__cc}" CFLAGS="%{rpmcflags}" \
LD="%{__cc} %{rpmldflags} -Wl,-s" \
DISPLAY_METHOD=x11 \
SOUND_ESOUND=1 \
SOUND_ALSA=1 \
SOUND_ARTS_TEIRA=1 \
SOUND_ARTS_SMOTEK=1 \
SOUND_SDL=1 

%{__make} -f makefile.unix \
PREFIX=%{_prefix} XMAMEROOT=$RPM_BUILD_ROOT%{_datadir}/games/%{name}
CC="%{__cc}" CFLAGS="%{rpmcflags}" \
LD="%{__cc} %{rpmldflags} -Wl,-s" \
DISPLAY_METHOD=svgalib \
SOUND_ESOUND=1 \
SOUND_ALSA=1 \
SOUND_ARTS_TEIRA=1 \
SOUND_ARTS_SMOTEK=1 \
SOUND_SDL=1

%{__make} -f makefile.unix \
PREFIX=%{_prefix} XMAMEROOT=$RPM_BUILD_ROOT%{_datadir}/games/%{name}
CC="%{__cc}" CFLAGS="%{rpmcflags}" \
LD="%{__cc} %{rpmldflags} -Wl,-s" \
DISPLAY_METHOD=SDL \
SOUND_ESOUND=1 \
SOUND_ALSA=1 \
SOUND_ARTS_TEIRA=1 \
SOUND_ARTS_SMOTEK=1 \
SOUND_SDL=1


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT $RPM_BUILD_ROOT{%{_bindir},%{_mandir},%{_pixmapsdir}} \
$RPM_BUILD_ROOT%{_datadir}/games/%{name} \
$RPM_BUILD_ROOT%{_datadir}/games/%{name}/cab \
$RPM_BUILD_ROOT%{_datadir}/games/%{name}/rc

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

install xmame.SDL $RPM_BUILD_ROOT%{_bindir}
install xmame.svgalib $RPM_BUILD_ROOT%{_bindir}
install xmame.x11 $RPM_BUILD_ROOT%{_bindir}

install src/unix/doc/xmame.6 $RPM_BUILD_ROOT%{_mandir}/man6

install contrib/tools/xmame-screensaver $RPM_BUILD_ROOT%{_bindir}

make -f makefile.unix XMAMEROOT=$RPM_BUILD_ROOT%{_datadir}/games/%{name} copycab



cp -r src/unix/doc/ $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

Ta wersja u¿ywa bibliotek svgalib dla wyj¶cia graficznego.
%files common
%defattr(644,root,root,755)
%doc src/unix/doc/*
%{_mandir}/man6/*
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/cab
%dir %{_datadir}/games/%{name}/rc
%{_datadir}/games/%{name}/cab/*
%{_pixmapsdir}/xmame.png

%files screensaver
%defattr(644,root,root,755)
%{_bindir}/xmame-screensaver

%files SDL
%defattr(644,root,root,755)
%{_bindir}/%{name}.SDL

%files svgalib
%defattr(644,root,root,755)
%{_bindir}/%{name}.svgalib

%files x11
%defattr(644,root,root,755)
%{_bindir}/%{name}.x11
