Name:		texlive-bibtex
Version:	0.99d
Release:	1
Summary:	Process bibliographies for LaTeX, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/base
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-kpathsea
Requires:	texlive-bibtex.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
BibTeX allows the user to store his citation data in generic
form, while printing citations in a document in the form
specified by a BibTeX style, to be specified in the document
itself. BibTeX itself is an ASCII-only program; there is,
however, a version that copes with 8-bit character sets.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/base/xampl.bib
%{_texmfdistdir}/bibtex/bst/base/abbrv.bst
%{_texmfdistdir}/bibtex/bst/base/acm.bst
%{_texmfdistdir}/bibtex/bst/base/alpha.bst
%{_texmfdistdir}/bibtex/bst/base/apalike.bst
%{_texmfdistdir}/bibtex/bst/base/ieeetr.bst
%{_texmfdistdir}/bibtex/bst/base/plain.bst
%{_texmfdistdir}/bibtex/bst/base/siam.bst
%{_texmfdistdir}/bibtex/bst/base/unsrt.bst
%doc %{_texmfdistdir}/doc/bibtex/base/README
%doc %{_texmfdistdir}/doc/bibtex/base/btxbst.doc
%doc %{_texmfdistdir}/doc/bibtex/base/btxdoc.bib
%doc %{_texmfdistdir}/doc/bibtex/base/btxdoc.pdf
%doc %{_texmfdistdir}/doc/bibtex/base/btxdoc.tex
%doc %{_texmfdistdir}/doc/bibtex/base/btxhak.pdf
%doc %{_texmfdistdir}/doc/bibtex/base/btxhak.tex
%doc %{_texmfdistdir}/tex/generic/bibtex/apalike.sty
%doc %{_texmfdistdir}/tex/generic/bibtex/apalike.tex
%doc %{_mandir}/man1/bibtex.1*
%doc %{_texmfdir}/doc/man/man1/bibtex.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1