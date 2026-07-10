%global tl_name bibtex
%global tl_revision 77830

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.99e
Release:	%{tl_revision}.1
Summary:	Process bibliographies (bib files) for LaTeX or other formats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/base
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(bibtex.bin)
Requires:	texlive(kpathsea)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
BibTeX allows the user to store his citation data in generic form, while
printing citations in a document in the form specified by a BibTeX
style, to be specified in the document itself (one often needs a LaTeX
citation-style package, such as natbib, as well). BibTeX knows nothing
about Unicode sorting algorithms or scripts, although it will pass on
whatever bytes it reads. Its descendant bibtexu does support Unicode,
via the ICU library. The older alternative bibtex8 supports 8-bit
character sets. Another Unicode-aware alternative is the (independently
developed) biber program, used with the BibLaTeX package to typeset its
output.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/tex
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex/bib
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/texmf-dist/doc/bibtex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man
%dir %{_datadir}/texmf-dist/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex/bib/base
%dir %{_datadir}/texmf-dist/texmf-dist/bibtex/bst/base
%dir %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/base
%dir %{_datadir}/texmf-dist/texmf-dist/doc/man/man1
%dir %{_datadir}/texmf-dist/texmf-dist/tex/generic/bibtex
%{_datadir}/texmf-dist/texmf-dist/bibtex/bib/base/xampl.bib
%{_datadir}/texmf-dist/texmf-dist/bibtex/bst/base/abbrv.bst
%{_datadir}/texmf-dist/texmf-dist/bibtex/bst/base/acm.bst
%{_datadir}/texmf-dist/texmf-dist/bibtex/bst/base/alpha.bst
%{_datadir}/texmf-dist/texmf-dist/bibtex/bst/base/apalike.bst
%{_datadir}/texmf-dist/texmf-dist/bibtex/bst/base/ieeetr.bst
%{_datadir}/texmf-dist/texmf-dist/bibtex/bst/base/plain.bst
%{_datadir}/texmf-dist/texmf-dist/bibtex/bst/base/siam.bst
%{_datadir}/texmf-dist/texmf-dist/bibtex/bst/base/unsrt.bst
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/base/README
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/base/btxbst.doc
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/base/btxdoc.bib
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/base/btxdoc.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/base/btxdoc.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/base/btxhak.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/bibtex/base/btxhak.tex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/bibtex.1
%doc %{_datadir}/texmf-dist/texmf-dist/doc/man/man1/bibtex.man1.pdf
%{_datadir}/texmf-dist/texmf-dist/tex/generic/bibtex/apalike.sty
%{_datadir}/texmf-dist/texmf-dist/tex/generic/bibtex/apalike.tex
