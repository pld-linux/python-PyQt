# TODO: check status of 64bit.patch (now is rejected).
%define		module	PyQt
%define		sipver	2:4.8
Summary:	Python bindings for the Qt toolkit
Summary(ko.UTF-8):	Qt의 파이썬 모듈
Summary(pl.UTF-8):	Dowiązania do toolkitu Qt dla Pythona
Name:		python-%{module}
Version:	3.18.1
Release:	2
License:	GPL v2
Group:		Libraries/Python
Source0:	http://www.riverbankcomputing.co.uk/static/Downloads/PyQt3/PyQt-x11-gpl-%{version}.tar.gz
# Source0-md5:	f1d120495d1aaf393819e988c0a7bb7e
# Patch0:		%{name}-64bit.patch
URL:		http://www.riverbankcomputing.co.uk/pyqt/index.php
BuildRequires:	OpenGL-devel
BuildRequires:	python-devel >= 2.2.2
BuildRequires:	python-sip-devel >= %{sipver}
BuildRequires:	qmake
BuildRequires:	qscintilla-devel >= 1:1.5
BuildRequires:	qt-designer-libs >= 3.3.0
BuildRequires:	qt-devel >= 6:3.3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	OpenGL
Requires:	python-sip >= %{sipver}
Requires:	qscintilla >= 1:1.7.1
Obsoletes:	%{module}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_sipfilesdir	%{_datadir}/sip

%description
PyQt is a set of Python bindings for the Qt toolkit. The bindings are
implemented as a set of Python modules: qt, qtcanvas, qtext, qtgl,
qtnetwork, qtsql, qttable, qtui and qtxml, and contains 300 classes
and over 5,750 functions and methods.

%description -l pl.UTF-8
PyQt to zbiór dowiązań do Qt dla Pythona. Dowiązania zostały
zaimplementowane jako moduły Pythona: qt, qtcanvas, qtext, qtgl,
qtnetwork, qtsql, qttable, qtui i qtxml - zawierają one 300 klas i
ponad 5 750 funkcji i metod.

%package devel
Summary:	Files needed to build other bindings based on Qt
Summary(pl.UTF-8):	Pliki potrzebne do budowania innych dowiązań bazowanych na Qt
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-sip-devel >= %{sipver}

%description devel
Files needed to build other bindings for C++ classes that inherit from
any of the Qt classes (e.g. KDE or your own).

%description devel -l pl.UTF-8
Pliki potrzebne do budowania innych dowiązań do klas C++
dziedziczących z dowolnej klasy Qt (np. KDE lub własnych).

%package examples
Summary:	Examples for PyQt
Summary(pl.UTF-8):	Przykłady do PyQt
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Examples code demonstrating how to use the Python bindings for Qt.

%description examples -l pl.UTF-8
Przykładowy kod demonstrujący jak używać PyQt.

%prep
%setup -q -n %{module}-x11-gpl-%{version}
#%%patch0 -p1

%build
export QMAKESPEC="%{_datadir}/qt/mkspecs/default"
echo 'yes' | python configure.py \
	-c -j 3 \
	-b %{_bindir} \
	-d %{py_sitedir} \
	-n %{_includedir}/qt \
	-o %{_libdir} \
	-q %{_prefix} \
	-v %{_sipfilesdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_sipfilesdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
cp -R examples3/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -R sip/* $RPM_BUILD_ROOT%{_sipfilesdir}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README THANKS doc/PyQt.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{py_sitedir}/*.so*
%{py_sitedir}/*.py[co]

%files devel
%defattr(644,root,root,755)
%{_sipfilesdir}/pyqt*.sip
%dir %{_sipfilesdir}/qt*
%{_sipfilesdir}/qt*/*.sip

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/*
