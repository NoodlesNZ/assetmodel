from assetmodel import DomainRecord

def test_domain_record():
    domain_record = DomainRecord(domain='example.com', name='example.com', extension='.com')

    assert domain_record.domain == 'example.com'
    assert domain_record.name == 'example.com'
    assert domain_record.extension == '.com'