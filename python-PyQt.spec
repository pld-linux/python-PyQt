%include	/usr/lib/rpm/macros.python
%define		module	PyQt
Summary:	Python bindings for the Qt toolkit
Summary(pl):	Dowi±zania do toolkitu Qt dla Pythona
Summary(ko):	QtÀÇ ÆÄÀÌ½ã ¸ðµâ
Name:		python-%{module}
Version:	3.11
%define         _snap           20040226
Release:	0.%{_snap}.1
License:	GPL
Group:		Libraries/Python
# Source0:	http://www.river-bank.demon.co.uk/download/PyQt/PyQt-x11-gpl-%{version}.tar.gz
Source0:	http://www.river-bank.demon.co.uk/download/snapshots/PyQt/PyQt-x11-gpl-snapshot-%{_snap}.tar.gz
# Source0-md5:	26aedc0406b58e6e96aaf17ff9512fcd
URL:		http://www.riverbankcomputing.co.uk/pyqt/index.php
BuildRequires:	OpenGL-devel
BuildRequires:	python-devel >= 2.2.2
BuildRequires:	qt-devel >= 3.1.2
BuildRequires:	qscintilla-devel >= 1:1.2
BuildRequires:	rpm-pythonprov
BuildRequires:	sip = 3.11
%requires_eq	sip
#Requires:	sip >= 3.11
%pyrequires_eq	python
Requires:	OpenGL
Requires:	qscintilla >= 1:1.2
Obsoletes:	%{module}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreqdep   libGL.so.1 libGLU.so.1
%define		sipdir		/usr/share/sip

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

%package devel
Summary:	Files needed to build other bindings based on Qt
Summary(pl):	Pliki potrzebne do budowania innych dowi±zañ bazowanych na Qt
Group:		Development/Languages/Python
Requires:	%{name} = %{version}
Requires:	sip

%description devel
Files needed to build other bindings for C++ classes that inherit from
any of the Qt classes (e.g. KDE or your own).

%description devel -l pl
Pliki potrzebne do budowania innych dowi±zañ do klas C++
dziedzicz±cych z dowolnej klasy Qt (np. KDE lub w³asnych).

%package examples
Summary:	Examples for PyQt
Summary(pl):	Przyklady do PyQt
Group:		Libraries/Python
Requires:	%{name} = %{version}

%description examples
Examples code demonstrating how to use the Python bindings for Qt.

%description examples -l pl
Przykladowy kod demonstruj±cy jak u¿ywaæ PyQT.

%prep
#%%setup -q -n %{module}-x11-gpl-%{version}
%setup -q -n %{module}-x11-gpl-snapshot-%{_snap}

%build

echo 'yes' | python configure.py \
	-c -j 3 \
	-b %{_bindir} \
	-n %{_includedir}/qt \
	-o %{_libdir} \
	-d %{py_sitedir} \
	-v %{sipdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/python/%{module},%{sipdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
cp -R examples3/* $RPM_BUILD_ROOT%{_examplesdir}/python/%{module}

cp -R sip/* $RPM_BUILD_ROOT%{sipdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README THANKS 
# doc/%{module}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{py_sitedir}/lib*.so*
%{py_sitedir}/*.py[co]

%files devel
%defattr(644,root,root,755)
%{sipdir}/*.sip
%{sipdir}/*/*.sip
%dir %{sipdir}/qt*
# ,qtcanvas,qtext,qtgl,qtnetwork,qtpe,qtsql,qttable,qtui,qtxml

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/python/%{module}
