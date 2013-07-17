Summary: Simple DirectMedia Layer - Sample Mixer Library
Name: SDL2_mixer
Version: 2.0.0
Release: 1
Source: http://www.libsdl.org/projects/%{name}/release/%{name}-%{version}.tar.gz
License: zlib
Group: System Environment/Libraries
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbisfile)
BuildRequires: pkgconfig(flac)

%description
Due to popular demand, here is a simple multi-channel audio mixer.
It supports 4 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular MikMod MOD, Timidity MIDI, Ogg Vorbis,
Tremor, SMPEG MP3, and libmad MP3 libraries.

%package devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/Libraries
Requires: %{name}

%description devel
Due to popular demand, here is a simple multi-channel audio mixer.
It supports 4 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular MikMod MOD, Timidity MIDI, Ogg Vorbis,
Tremor, SMPEG MP3, and libmad MP3 libraries.

%prep
%setup -q

%build
%configure
make

%install
%make_install

%files
%defattr(-,root,root)
%doc README.txt CHANGES.txt COPYING.txt
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc README.txt CHANGES.txt COPYING.txt
%{_libdir}/lib*.so
%{_includedir}/*/*.h
%{_libdir}/pkgconfig/*

