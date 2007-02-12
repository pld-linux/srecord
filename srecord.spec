Summary:	Manipulate EPROM load files
Summary(pl.UTF-8):   Operacje na plikach do programowania pamięci (E)EPROM i Flash
Name:		srecord
Version:	1.23
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://srecord.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	fcca798d3cc3f186410b8ed0e1c2e793
Patch0:		%{name}-man_fastload.patch
URL:		http://srecord.sourceforge.net/
BuildRequires:  bison
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SRecord package is a collection of powerful tools for manipulating
EPROM load files.

- The SRecord package understands a number of file formats: Motorola
  S-Record, Intel, Tektronix, Binary. These file formats may be read and
  written. Also C array definitions, for output only.

- The SRecord package has a number of tools: srec_cat for copying and
  and converting files, srec_cmp for comparing files and srec_info for
  printing summaries.

- The SRecord package has a number for filters: checksum to add
  checksums to the data, crop to keep address ranges, exclude to remove
  address ranges, fill to plug holes in the data, length to insert the
  data length, maximum to insert the data address maximum, minimum to
  insert the data address minimum, offset to adjust addresses, and split
  for wide data buses and memory striping.

More than one filter may be applied to each input file. Different
filters may be applied to each input file. All filters may be applied
to all file formats.

%description -l pl.UTF-8
Pakiet SRecord to zbiór narzędzi do modyfikacji plików używanych do
programowania pamięci (E)EPROM i Flash.

- Odczytywane i zapisywane są pliki w następujących formatach:
  Motorola S-Record, Intel, Tektronix, Binary.

- W pakiecie znajdują się następujące narzędzia: srec_cat - do
  kopiowania i konwersji plików, srec_cmp - do porównywania plików,
  srec_info - do wyświetlania informacji o plikach.

- Dostępne są następujące filtry: cheksum - dodawanie sumy kontrolnej
  do danych, crop - usuwanie danych spoza podanego zakresu adresów,
  exclude - usuwanie danych z podanego zakresu adresów, fill -
  wypełnianie podanego zakresu adresów, length - dodawanie długości
  danych, maximum - dodawanie największego adresu z danych wejściowych,
  minimum - dodawanie najmniejszego adresu z danych wejściowych, offset
  - modyfikowanie adresów o podaną wartość, split - rozdzielanie danych
  wejściowych na podzbiory.

Dla każdego pliku wejściowego może być dodanych po kilka filtrów
wejściowych. Każdy z filtrów może być stosowany do każdego z formatów
plików.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUILDING README
%attr(755,root,root) %{_bindir}/srec_cat
%attr(755,root,root) %{_bindir}/srec_cmp
%attr(755,root,root) %{_bindir}/srec_info
%{_mandir}/man1/*
%{_mandir}/man5/*
