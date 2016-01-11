#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Test
%define		pnam	SharedFork
%include	/usr/lib/rpm/macros.perl
Summary:	Test::SharedFork - fork test
Summary(pl.UTF-8):	Test::SharedFork - testowanie funkcji fork
Name:		perl-Test-SharedFork
Version:	0.35
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3101aea2e3ae41d48fd8874414430cef
URL:		http://search.cpan.org/dist/Test-SharedFork/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.64
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::SharedFork is utility module for Test::Builder.

This module makes fork(2) safety in your test case.

This module merges test count with parent process & child process.

%description -l pl.UTF-8
Test::SharedFork to moduł narzędziowy dla modułu Test::Builder.

Ten moduł czyni wywołanie fork(2) bezpiecznym w przypadkach testowych.
Łączy liczbę testów z procesu rodzica z procesami potomnymi.

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
%doc Changes README.md
%{perl_vendorlib}/Test/SharedFork.pm
%{perl_vendorlib}/Test/SharedFork
%{_mandir}/man3/Test::SharedFork.3pm*
