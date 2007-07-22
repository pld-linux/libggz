Summary:	Makes free online gaming possible
Summary(pl.UTF-8):	Pozwala grać online w darmowe gry
Name:		libggz
Version:	0.0.14
Release:	1
License:	GPL v2.1+
Group:		Libraries
Source0:	http://ftp.belnet.be/packages/ggzgamingzone/ggz/0.0.14/%{name}-%{version}.tar.gz
# Source0-md5:	dfd0039042e1bc6c899faaa63d56dad1
URL:		http://www.ggzgamingzone.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the GGZ base library libggz, used by the GGZ Gaming Zone server (ggzd), the ggzcore library and other components.

%description -l pl.UTF-8
To jest podstawowa biblioteka projektu GGZ - libggz, użyana przez serwer GGZ Gaming Zone (ggzd), bibliotekę ggzcore oraz inne komponenty.

%package devel
Summary:	Header files for libggz library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libggz
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
eader files for libggz library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libggz.

%package static
Summary:	Static libggz library
Summary(pl.UTF-8):	Statyczna biblioteka libggz
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libggz library.

%description static -l pl.UTF-8
Statyczna biblioteka libggz.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man3/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
