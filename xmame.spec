# $Revision: 1.2 $
Summary:	Unix/X11 port of M.A.M.E. - arcade machine emulator
Summary(pl):	Port emulatora M.A.M.E. dzia³aj±cy w ¶rodowisku Unix/X11
Name:		xmame
Version:	0.60.1	
Release:	0.1
License:	GPL
Group:		X11/Emulators
Source0:	%{name}-%{version}.tar.bz2
URL:		http://x.mame.net
BuildRequires:	alsa-driver-devel XFree86-devel zlib-devel
#Requires:	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man

%description
Unix/X11 port of M.A.M.E. - arcade machine emulator

%description -l pl
Port emulatora M.A.M.E. dzia³aj±cy w ¶rodowisku Unix/X11

%package SDL
Summary:	xmame - SDL version
Summary(pl):	xmame - wersja z wyj¶ciem SDL
Group:          X11/Emulators
Requires: 	SDL 
BuildRequires:	SDL-devel

%description SDL
Unix/X11 port of M.A.M.E. - arcade machine emulator.
This version uses SDL for graphic output.
%description SDL -l pl
Port emulatora M.A.M.E. dzia³aj±cy w ¶rodowisku Unix/X11
Ta wersja u¿ywa bibliotek SDL dla wyj¶cia graficznego.

%package svgalib
Summary:        xmame - svgalib version
Summary(pl):    xmame - wersja z wyj¶ciem svgalib
Group:          X11/Emulators
Requires:       svgalib
BuildRequires:  svgalib-devel

%description svgalib
Unix/X11 port of M.A.M.E. - arcade machine emulator.
This version uses svgalib for graphic output.
%description svgalib -l pl
Port emulatora M.A.M.E. dzia³aj±cy w ¶rodowisku Unix/X11
Ta wersja u¿ywa bibliotek svgalib dla wyj¶cia graficznego.


%package x11 
Summary:        xmame - x11 version
Summary(pl):    xmame - wersja z wyj¶ciem x11
Group:          X11/Emulators
Requires:       XFree86-libs
#BuildRequires:  

%description x11
Unix/X11 port of M.A.M.E. - arcade machine emulator. 
This version uses x11 for graphic output.

%description x11 -l pl
Port emulatora M.A.M.E. dzia³aj±cy w ¶rodowisku Unix/X11
Ta wersja u¿ywa x11 dla wyj¶cia graficznego.

%package x11
Summary:        xmame - x11 version
Summary(pl):    xmame - wersja z wyj¶ciem x11
Group:          X11/Emulators
Requires:       XFree86-libs
#BuildRequires:  

%description x11
Unix/X11 port of M.A.M.E. - arcade machine emulator.
This version uses x11 for graphic output.

%description x11 -l pl
Port emulatora M.A.M.E. dzia³aj±cy w ¶rodowisku Unix/X11
Ta wersja zosta³a skompilowana z obs³ug± OpenGL.

%prep

%setup -q
#%patch0 -p1

%build

%{__make} -f makefile.unix \
PREFIX=%{_prefix} XMAMEROOT=%{_sysconfdir}/xmame
CC="%{__cc}" CFLAGS="%{rpmcflags}" \
LD="%{__cc} %{rpmldflags} -Wl,-s" \
DISPLAY_METHOD=x11 \
SOUND_ESOUND = 1 \
SOUND_ALSA = 1 \
SOUND_ARTS_TEIRA = 1 \
SOUND_ARTS_SMOTEK = 1 \
SOUND_SDL= 1 

make -f makefile.unix XMAMEROOT=%buildroot%{_libdir}/games/%{name} copycab


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT $RPM_BUILD_ROOT{%{_bindir},%{_mandir}} \
$RPM_BUILD_ROOT%{_datadir}/games/%{name} \
$RPM_BUILD_ROOT%{_datadir}/games/%{name}/cab

install xmame.SDL $RPM_BUILD_ROOT%{_bindir}
install xmame.svgalib $RPM_BUILD_ROOT%{_bindir}
install xmame.x11 $RPM_BUILD_ROOT%{_bindir}

install src/unix/doc/xmame.6 $RPM_BUILD_ROOT%{_mandir}/man6

install contrib/tools/xmame-screensaver $RPM_BUILD_ROOT%{_bindir}

make -f makefile.unix XMAMEROOT=$RPM_BUILD_ROOT%{_datadir}/games/%{name} copycab

cp -r src/unix/doc/ $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc src/unix/doc/*
%{_mandir}/man6/*
%{_bindir}/xmame-screensaver
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/cab

%files SDL
%defattr(644,root,root,755)
%{_bindir}/%{name}.SDL

%files svgalib
%defattr(644,root,root,755)
%{_bindir}/%{name}.svgalib

%files x11
%defattr(644,root,root,755)
%{_bindir}/%{name}.x11
