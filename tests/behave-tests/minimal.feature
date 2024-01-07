Feature: Minimal interface

    Scenario: Method call without arguments or return value
        Given a mocked backend service 'Bob'
         And a running python service
         And a mocked python client 'Alice'
        When the 'Bump' method is called by 'Alice'
        Then 'Bob' receives a 'Bump' method call

    Scenario: Signal without arguments
        Given a mocked backend service 'Bob'
         And a running python service
         And a mocked python client 'Alice'
        When a 'Bumped' signal is emitted by 'Bob'
        Then 'Alice' receives a 'Bumped' signal
