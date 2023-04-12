file = input()
with open(f'{file}', 'r') as f:
    file_content = f.readlines()

dna = file_content[0].strip()
dna_restriction_site = file_content[1].strip()
gfp = file_content[2].strip()
gfp_restriction_sites = file_content[3].split(' ')
gfp_restriction_left = gfp_restriction_sites[0].strip()
gfp_restriction_right = gfp_restriction_sites[1].strip()

principle = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

comp_dna_list = []
comp_dna_restriction_site_list = []
comp_gfp_list = []
comp_gfp_restriction_left_list = []
comp_gfp_restriction_right_list = []


def complement(strand, comp_strand_list):
    for i in strand:
        comp_strand_list.append(principle[i])
    return ''.join(comp_strand_list)


comp_dna = complement(dna, comp_dna_list)
comp_dna_restriction_site = complement(dna_restriction_site, comp_dna_restriction_site_list)
comp_gfp = complement(gfp, comp_gfp_list)
comp_gfp_restriction_left = complement(gfp_restriction_left, comp_gfp_restriction_left_list)
comp_gfp_restriction_right = complement(gfp_restriction_right, comp_gfp_restriction_right_list)


def cut_normal_plasmid(dna_strand, restrict_site):
    cut_index = dna_strand.index(restrict_site)
    return dna_strand[:cut_index + 1] + ' ' + dna_strand[cut_index + 1:]


def cut_comp_plasmid(dna_strand, restrict_site):
    cut_index = dna_strand.index(restrict_site)
    return dna_strand[:cut_index + 5] + ' ' + dna_strand[cut_index + 5:]


def comp_gfp_slice(gfp_dna, comp_restriction_site_left, comp_restriction_site_right):
    split_left = gfp_dna.index(comp_restriction_site_left)
    split_right = gfp_dna.index(comp_restriction_site_right)
    return gfp_dna[split_left + 5:split_right + 5]


def gfp_slice(gfp_dna, restriction_site_left, restriction_site_right):
    split_left = gfp_dna.index(restriction_site_left)
    split_right = gfp_dna.index(restriction_site_right)
    return gfp_dna[split_left + 1:split_right + 1]


mod_original_plasmid = cut_normal_plasmid(dna, dna_restriction_site)
mod_comp_plasmid = cut_comp_plasmid(comp_dna, comp_dna_restriction_site)

print(mod_original_plasmid.replace(' ', gfp_slice(gfp, gfp_restriction_left, gfp_restriction_right)))
print(mod_comp_plasmid.replace(' ', comp_gfp_slice(comp_gfp, comp_gfp_restriction_left, comp_gfp_restriction_right)))
