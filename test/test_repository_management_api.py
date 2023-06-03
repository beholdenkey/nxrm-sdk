# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.42.0-01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import nxrm_sdk
from nxrm_sdk.api.repository_management_api import RepositoryManagementApi  # noqa: E501
from nxrm_sdk.rest import ApiException


class TestRepositoryManagementApi(unittest.TestCase):
    """RepositoryManagementApi unit test stubs"""

    def setUp(self):
        self.api = RepositoryManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_repository(self):
        """Test case for create_repository

        Create Maven group repository  # noqa: E501
        """
        pass

    def test_create_repository1(self):
        """Test case for create_repository1

        Create Maven hosted repository  # noqa: E501
        """
        pass

    def test_create_repository10(self):
        """Test case for create_repository10

        Create npm proxy repository  # noqa: E501
        """
        pass

    def test_create_repository11(self):
        """Test case for create_repository11

        Create NuGet group repository  # noqa: E501
        """
        pass

    def test_create_repository12(self):
        """Test case for create_repository12

        Create NuGet hosted repository  # noqa: E501
        """
        pass

    def test_create_repository13(self):
        """Test case for create_repository13

        Create NuGet proxy repository  # noqa: E501
        """
        pass

    def test_create_repository14(self):
        """Test case for create_repository14

        Create RubyGems group repository  # noqa: E501
        """
        pass

    def test_create_repository15(self):
        """Test case for create_repository15

        Create RubyGems hosted repository  # noqa: E501
        """
        pass

    def test_create_repository16(self):
        """Test case for create_repository16

        Create RubyGems proxy repository  # noqa: E501
        """
        pass

    def test_create_repository17(self):
        """Test case for create_repository17

        Create Yum group repository  # noqa: E501
        """
        pass

    def test_create_repository18(self):
        """Test case for create_repository18

        Create Yum hosted repository  # noqa: E501
        """
        pass

    def test_create_repository19(self):
        """Test case for create_repository19

        Create Yum proxy repository  # noqa: E501
        """
        pass

    def test_create_repository2(self):
        """Test case for create_repository2

        Create Maven proxy repository  # noqa: E501
        """
        pass

    def test_create_repository20(self):
        """Test case for create_repository20

        Create Docker group repository  # noqa: E501
        """
        pass

    def test_create_repository21(self):
        """Test case for create_repository21

        Create Docker hosted repository  # noqa: E501
        """
        pass

    def test_create_repository22(self):
        """Test case for create_repository22

        Create Docker proxy repository  # noqa: E501
        """
        pass

    def test_create_repository23(self):
        """Test case for create_repository23

        Create PyPI group repository  # noqa: E501
        """
        pass

    def test_create_repository24(self):
        """Test case for create_repository24

        Create PyPI hosted repository  # noqa: E501
        """
        pass

    def test_create_repository25(self):
        """Test case for create_repository25

        Create PyPI proxy repository  # noqa: E501
        """
        pass

    def test_create_repository26(self):
        """Test case for create_repository26

        Create conda proxy repository  # noqa: E501
        """
        pass

    def test_create_repository27(self):
        """Test case for create_repository27

        Create Conan proxy repository  # noqa: E501
        """
        pass

    def test_create_repository28(self):
        """Test case for create_repository28

        Create Git LFS hosted repository  # noqa: E501
        """
        pass

    def test_create_repository29(self):
        """Test case for create_repository29

        Create R group repository  # noqa: E501
        """
        pass

    def test_create_repository3(self):
        """Test case for create_repository3

        Create APT hosted repository  # noqa: E501
        """
        pass

    def test_create_repository30(self):
        """Test case for create_repository30

        Create R hosted repository  # noqa: E501
        """
        pass

    def test_create_repository31(self):
        """Test case for create_repository31

        Create R proxy repository  # noqa: E501
        """
        pass

    def test_create_repository32(self):
        """Test case for create_repository32

        Create Cocoapods proxy repository  # noqa: E501
        """
        pass

    def test_create_repository33(self):
        """Test case for create_repository33

        Create a Go group repository  # noqa: E501
        """
        pass

    def test_create_repository34(self):
        """Test case for create_repository34

        Create a Go proxy repository  # noqa: E501
        """
        pass

    def test_create_repository35(self):
        """Test case for create_repository35

        Create p2 proxy repository  # noqa: E501
        """
        pass

    def test_create_repository36(self):
        """Test case for create_repository36

        Create Helm hosted repository  # noqa: E501
        """
        pass

    def test_create_repository37(self):
        """Test case for create_repository37

        Create Helm proxy repository  # noqa: E501
        """
        pass

    def test_create_repository38(self):
        """Test case for create_repository38

        Create Bower group repository  # noqa: E501
        """
        pass

    def test_create_repository39(self):
        """Test case for create_repository39

        Create Bower hosted repository  # noqa: E501
        """
        pass

    def test_create_repository4(self):
        """Test case for create_repository4

        Create APT proxy repository  # noqa: E501
        """
        pass

    def test_create_repository40(self):
        """Test case for create_repository40

        Create Bower proxy repository  # noqa: E501
        """
        pass

    def test_create_repository5(self):
        """Test case for create_repository5

        Create raw group repository  # noqa: E501
        """
        pass

    def test_create_repository6(self):
        """Test case for create_repository6

        Create raw hosted repository  # noqa: E501
        """
        pass

    def test_create_repository7(self):
        """Test case for create_repository7

        Create raw proxy repository  # noqa: E501
        """
        pass

    def test_create_repository8(self):
        """Test case for create_repository8

        Create npm group repository  # noqa: E501
        """
        pass

    def test_create_repository9(self):
        """Test case for create_repository9

        Create npm hosted repository  # noqa: E501
        """
        pass

    def test_delete_repository(self):
        """Test case for delete_repository

        Delete repository of any format  # noqa: E501
        """
        pass

    def test_disable_repository_health_check(self):
        """Test case for disable_repository_health_check

        Disable repository health check. Proxy repositories only.  # noqa: E501
        """
        pass

    def test_enable_repository_health_check(self):
        """Test case for enable_repository_health_check

        Enable repository health check. Proxy repositories only.  # noqa: E501
        """
        pass

    def test_get_repositories(self):
        """Test case for get_repositories

        List repositories  # noqa: E501
        """
        pass

    def test_get_repositories1(self):
        """Test case for get_repositories1

        List repositories  # noqa: E501
        """
        pass

    def test_get_repository(self):
        """Test case for get_repository

        Get repository details  # noqa: E501
        """
        pass

    def test_get_repository1(self):
        """Test case for get_repository1

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository10(self):
        """Test case for get_repository10

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository11(self):
        """Test case for get_repository11

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository12(self):
        """Test case for get_repository12

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository13(self):
        """Test case for get_repository13

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository14(self):
        """Test case for get_repository14

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository15(self):
        """Test case for get_repository15

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository16(self):
        """Test case for get_repository16

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository17(self):
        """Test case for get_repository17

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository18(self):
        """Test case for get_repository18

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository19(self):
        """Test case for get_repository19

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository2(self):
        """Test case for get_repository2

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository20(self):
        """Test case for get_repository20

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository21(self):
        """Test case for get_repository21

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository22(self):
        """Test case for get_repository22

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository23(self):
        """Test case for get_repository23

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository24(self):
        """Test case for get_repository24

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository25(self):
        """Test case for get_repository25

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository26(self):
        """Test case for get_repository26

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository27(self):
        """Test case for get_repository27

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository28(self):
        """Test case for get_repository28

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository29(self):
        """Test case for get_repository29

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository3(self):
        """Test case for get_repository3

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository30(self):
        """Test case for get_repository30

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository31(self):
        """Test case for get_repository31

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository32(self):
        """Test case for get_repository32

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository33(self):
        """Test case for get_repository33

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository34(self):
        """Test case for get_repository34

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository35(self):
        """Test case for get_repository35

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository36(self):
        """Test case for get_repository36

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository37(self):
        """Test case for get_repository37

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository38(self):
        """Test case for get_repository38

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository39(self):
        """Test case for get_repository39

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository4(self):
        """Test case for get_repository4

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository40(self):
        """Test case for get_repository40

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository41(self):
        """Test case for get_repository41

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository5(self):
        """Test case for get_repository5

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository6(self):
        """Test case for get_repository6

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository7(self):
        """Test case for get_repository7

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository8(self):
        """Test case for get_repository8

        Get repository  # noqa: E501
        """
        pass

    def test_get_repository9(self):
        """Test case for get_repository9

        Get repository  # noqa: E501
        """
        pass

    def test_invalidate_cache(self):
        """Test case for invalidate_cache

        Invalidate repository cache. Proxy or group repositories only.  # noqa: E501
        """
        pass

    def test_rebuild_index(self):
        """Test case for rebuild_index

        Schedule a 'Repair - Rebuild repository search' Task. Hosted or proxy repositories only.  # noqa: E501
        """
        pass

    def test_update_repository(self):
        """Test case for update_repository

        Update Maven group repository  # noqa: E501
        """
        pass

    def test_update_repository1(self):
        """Test case for update_repository1

        Update Maven hosted repository  # noqa: E501
        """
        pass

    def test_update_repository10(self):
        """Test case for update_repository10

        Update npm proxy repository  # noqa: E501
        """
        pass

    def test_update_repository11(self):
        """Test case for update_repository11

        Update NuGet group repository  # noqa: E501
        """
        pass

    def test_update_repository12(self):
        """Test case for update_repository12

        Update NuGet hosted repository  # noqa: E501
        """
        pass

    def test_update_repository13(self):
        """Test case for update_repository13

        Update NuGet proxy repository  # noqa: E501
        """
        pass

    def test_update_repository14(self):
        """Test case for update_repository14

        Update RubyGems group repository  # noqa: E501
        """
        pass

    def test_update_repository15(self):
        """Test case for update_repository15

        Update RubyGems hosted repository  # noqa: E501
        """
        pass

    def test_update_repository16(self):
        """Test case for update_repository16

        Update RubyGems proxy repository  # noqa: E501
        """
        pass

    def test_update_repository17(self):
        """Test case for update_repository17

        Update Yum group repository  # noqa: E501
        """
        pass

    def test_update_repository18(self):
        """Test case for update_repository18

        Update Yum hosted repository  # noqa: E501
        """
        pass

    def test_update_repository19(self):
        """Test case for update_repository19

        Update Yum proxy repository  # noqa: E501
        """
        pass

    def test_update_repository2(self):
        """Test case for update_repository2

        Update Maven proxy repository  # noqa: E501
        """
        pass

    def test_update_repository20(self):
        """Test case for update_repository20

        Update Docker group repository  # noqa: E501
        """
        pass

    def test_update_repository21(self):
        """Test case for update_repository21

        Update Docker hosted repository  # noqa: E501
        """
        pass

    def test_update_repository22(self):
        """Test case for update_repository22

        Update Docker group repository  # noqa: E501
        """
        pass

    def test_update_repository23(self):
        """Test case for update_repository23

        Update PyPI group repository  # noqa: E501
        """
        pass

    def test_update_repository24(self):
        """Test case for update_repository24

        Update PyPI hosted repository  # noqa: E501
        """
        pass

    def test_update_repository25(self):
        """Test case for update_repository25

        Update PyPI proxy repository  # noqa: E501
        """
        pass

    def test_update_repository26(self):
        """Test case for update_repository26

        Update conda proxy repository  # noqa: E501
        """
        pass

    def test_update_repository27(self):
        """Test case for update_repository27

        Update Conan proxy repository  # noqa: E501
        """
        pass

    def test_update_repository28(self):
        """Test case for update_repository28

        Update Git LFS hosted repository  # noqa: E501
        """
        pass

    def test_update_repository29(self):
        """Test case for update_repository29

        Update R group repository  # noqa: E501
        """
        pass

    def test_update_repository3(self):
        """Test case for update_repository3

        Update APT hosted repository  # noqa: E501
        """
        pass

    def test_update_repository30(self):
        """Test case for update_repository30

        Update R hosted repository  # noqa: E501
        """
        pass

    def test_update_repository31(self):
        """Test case for update_repository31

        Update R proxy repository  # noqa: E501
        """
        pass

    def test_update_repository32(self):
        """Test case for update_repository32

        Update Cocoapods proxy repository  # noqa: E501
        """
        pass

    def test_update_repository33(self):
        """Test case for update_repository33

        Update a Go group repository  # noqa: E501
        """
        pass

    def test_update_repository34(self):
        """Test case for update_repository34

        Update a Go proxy repository  # noqa: E501
        """
        pass

    def test_update_repository35(self):
        """Test case for update_repository35

        Update p2 proxy repository  # noqa: E501
        """
        pass

    def test_update_repository36(self):
        """Test case for update_repository36

        Update Helm hosted repository  # noqa: E501
        """
        pass

    def test_update_repository37(self):
        """Test case for update_repository37

        Update Helm proxy repository  # noqa: E501
        """
        pass

    def test_update_repository38(self):
        """Test case for update_repository38

        Update Bower group repository  # noqa: E501
        """
        pass

    def test_update_repository39(self):
        """Test case for update_repository39

        Update Bower hosted repository  # noqa: E501
        """
        pass

    def test_update_repository4(self):
        """Test case for update_repository4

        Update APT proxy repository  # noqa: E501
        """
        pass

    def test_update_repository40(self):
        """Test case for update_repository40

        Update Bower proxy repository  # noqa: E501
        """
        pass

    def test_update_repository5(self):
        """Test case for update_repository5

        Update raw group repository  # noqa: E501
        """
        pass

    def test_update_repository6(self):
        """Test case for update_repository6

        Update raw hosted repository  # noqa: E501
        """
        pass

    def test_update_repository7(self):
        """Test case for update_repository7

        Update raw proxy repository  # noqa: E501
        """
        pass

    def test_update_repository8(self):
        """Test case for update_repository8

        Update npm group repository  # noqa: E501
        """
        pass

    def test_update_repository9(self):
        """Test case for update_repository9

        Update npm hosted repository  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
