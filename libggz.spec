Summary:	Makes free online gaming possible
Summary(pl.UTF-8):	Biblioteka pozwalająca grać online w darmowe gry
Name:		libggz
Version:	0.0.14.1
Release:	3
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.belnet.be/packages/ggzgamingzone/ggz/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	603739504648833779aa13b0327a1c3d
Patch0:		%{name}-link.patch
URL:		http://www.ggzgamingzone.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gnutls-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the GGZ base library libggz, used by the GGZ Gaming Zone
server (ggzd), the ggzcore library and other components.

%description -l pl.UTF-8
To jest podstawowa biblioteka projektu GGZ - libggz, używana przez
serwer GGZ Gaming Zone (ggzd), bibliotekę ggzcore oraz inne
komponenty.

%package devel
Summary:	Header files for libggz library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libggz
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnutls-devel
Requires:	libgcrypt-devel

%description devel
Header files for libggz library.

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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I m4/ggz
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-gcrypt \
	--with-gnutls-libraries=%{_libdir} \
	--with-tls
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/ggz

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README*
%attr(755,root,root) %{_libdir}/libggz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libggz.so.2
%dir %{_datadir}/ggz

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libggz.so
%{_libdir}/libggz.la
%{_includedir}/ggz.h
%{_includedir}/ggz_common.h
%{_includedir}/ggz_dio.h
%{_mandir}/man3/ggz.h.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libggz.a
