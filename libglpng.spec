Summary:	PNG loader library for OpenGL
Summary(pl):	Biblioteka Ёaduj╠ca PNG dla OpenGL
Name:		libglpng
Version:	1.45
Release:	1
License:	BSD
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/Библиотеки
Group(uk):	X11/Б╕бл╕отеки
Source0:	http://www.wyatt100.freeserve.co.uk/glpng.zip
Patch0:		%{name}-debian.patch
URL:		http://www.fachschaften.neuphilologie.uni-tuebingen.de/doc/libglpng/glpng.html
BuildRequires:	OpenGL-devel
BuildRequires:	libpng-devel
BuildRequires:	unzip
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6

%description
This is a library for OpenGL to load PNG graphics files as an OpenGL
texture as easily as possible.

%description -l pl
To jest biblioteka dla OpenGL pozwalaj╠ca ЁadowaФ grafikЙ PNG jako
tekstury OpenGL.

%package devel
Summary:	Libraries, includes, etc to develop libglpng applications
Summary(pl):	Pliki developerskie libglpng
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}
Requires:	OpenGL-devel

%description devel
Libraries, includes, etc to develop libglpng applications.

%description -l pl devel
Pliki developerskie libglpng.

%package static
Summary:	Static libglpng library
Summary(pl):	Biblioteka statyczna libglpng
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
Static libglpng library.

%description -l pl static
Biblioteka statyczna libglpng.

%prep
%setup -q -c -n %{name}-%{version}
%patch0 -p1

%build
%{__make} CC="%{__cc}" OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT%{_prefix}

rm -f Example/*.exe

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.htm
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc Example/*
%{_includedir}/GL/*.h
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
