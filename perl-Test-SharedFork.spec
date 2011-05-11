#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	SharedFork
%include	/usr/lib/rpm/macros.perl
Summary:	Test::SharedFork - fork test
#Summary(pl.UTF-8):	
Name:		perl-Test-SharedFork
Version:	0.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ee0469b14d48bbd651f2ec5465f61a52
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Test-SharedFork/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::SharedFork is utility module for Test::Builder.

This module makes fork(2) safety in your test case.

This module merges test count with parent process & child process.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/*.pm
%{perl_vendorlib}/Test/SharedFork
%{_mandir}/man3/*
