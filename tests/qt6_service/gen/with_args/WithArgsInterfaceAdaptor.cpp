/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/02.1_with_args.yml
 *   Object: WithArgs
 *   Template: qt6/service_source.j2
 */
#include "WithArgsInterfaceAdaptor.hpp"

using namespace gen::with_args;

WithArgsInterfaceAdaptor::WithArgsInterfaceAdaptor(WithArgsInterface* iface, QObject* parent) : m_iface(iface), QDBusAbstractAdaptor(parent) {

}

void WithArgsInterfaceAdaptor::Notify(
    QString message,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleNotifyCalled(_message);
}

double WithArgsInterfaceAdaptor::Order(
    QString item,
    uint amount,
    double pricePerItem,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleOrderCalled(_message);
    return {};
}

double WithArgsInterfaceAdaptor::getSpeed() const {
    auto value = m_iface->getSpeed();
    return value;
}

void WithArgsInterfaceAdaptor::setSpeed(const double &value ) {
    emit m_iface->propertySpeedSet(value);
}

uint WithArgsInterfaceAdaptor::getDistance() const {
    auto value = m_iface->getDistance();
    return value;
}

void WithArgsInterfaceAdaptor::setDistance(const uint &value ) {
    emit m_iface->propertyDistanceSet(value);
}

double WithArgsInterfaceAdaptor::getDuration() const {
    auto value = m_iface->getDuration();
    return value;
}

