%include	/usr/lib/rpm/macros.python
%define		module	PyQt
Summary:	Python bindings for the Qt toolkit
Summary(pl):	Dowi±zania do toolkitu Qt dla Pythona
Name:		python-%{module}
Version:	3.1
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://www.riverbankcomputing.co.uk/download/PyQt/PyQt-%{version}-Qt-3.0.2.tar.gz
Patch0:		http://www.riverbankcomputing.co.uk/download/PyQt/PyQt-3.1-patch.1
URL:		http://www.riverbankcomputing.co.uk/pyqt/index.php
Requires:	OpenGL
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	qt-devel >= 3.0.2
BuildRequires:	rpm-pythonprov
BuildRequires:	sip >= 3.1
%requires_eq	sip
%pyrequires_eq	python
Obsoletes:	%{module}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreqdep   libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
PyQt is a set of Python bindings for the Qt toolkit. The bindings are
implemented as a set of Python modules: qt, qtcanvas, qtgl, qtnetwork,
qtsql, qttable and qtxml, and contains 300 classes and over 5,750
functions and methods.

%description -l pl
PyQT to zbiór dowi±zañ do Qt dla Pythona. Dowi±zania zosta³y
zaimplementowane jako modu³y Pythona: qt, qtcanvas, qtgl, qtnetwork,
qtsql, qttable i qtxml - zawieraj± one 300 klas i ponad 5 750 funkcji
i metod.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%configure \
	--with-qt-includes=%{_includedir}/qt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-sip install-doc \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

gzip -9nf NEWS README THANKS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/%{module}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{py_sitedir}/lib*.so
%{py_sitedir}/lib*.la
%{py_sitedir}/eric
%{py_sitedir}/*.py[co]
%{_datadir}/sip/qt
